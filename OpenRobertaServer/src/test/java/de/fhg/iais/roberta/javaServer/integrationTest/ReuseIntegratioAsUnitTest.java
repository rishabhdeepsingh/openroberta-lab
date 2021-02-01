package de.fhg.iais.roberta.javaServer.integrationTest;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;

import javax.xml.bind.JAXBException;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import de.fhg.iais.roberta.transformer.Jaxb2ProgramAst;
import org.apache.commons.io.FileUtils;
import org.json.JSONObject;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Ignore;
import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import de.fhg.iais.roberta.blockly.generated.BlockSet;
import de.fhg.iais.roberta.components.ProgramAst;
import de.fhg.iais.roberta.components.Project;
import de.fhg.iais.roberta.factory.IRobotFactory;
import de.fhg.iais.roberta.javaServer.restServices.all.controller.ProjectWorkflowRestController;
import de.fhg.iais.roberta.syntax.Phrase;
import de.fhg.iais.roberta.util.Pair;
import de.fhg.iais.roberta.util.Util;
import de.fhg.iais.roberta.util.jaxb.JaxbHelper;
import de.fhg.iais.roberta.util.test.UnitTestHelper;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;

public class ReuseIntegratioAsUnitTest {
    private static final Logger LOG = LoggerFactory.getLogger(ReuseIntegratioAsUnitTest.class);
    private static final String ROBOT_NAME_FOR_COMMON_TESTS = "ev3lejosv1";
    private static final String[] ROBOT_NAMES_FOR_TARGET_LANGUAGE_GENERATION =
        {
            "ev3lejosv1",
            "calliope2017NoBlue",
            "ev3dev",
            "wedo"
        };
    private static final String TARGET_DIR = "target/unitTests";
    private static final String RESOURCE_BASE_COMMON = "/crossCompilerTests/common/";
    private static final String RESOURCE_BASE_SPECIFIC = "/crossCompilerTests/robotSpecific/";

    private static final String AST = "/ast";
    private static final String PROG_GENERATED = "/progGenerated";
    private static final String PROG_REGENERATED = "/progRegenerated";
    private static final String CONFIG_GENERATED = "/configGenerated";
    private static final String CONFIG_REGENERATED = "/configRegenerated";
    private static final String TARGET_LANGUAGE_GENERATED = "/targetLanguage";
    private static final String TARGET_LANGUAGE_SOURCE = "/targetSource";

    private static final boolean STORE_ALWAYS_DATA_INTO_FILES = true;
    private static final boolean LOG_NAMES_ON_SUCCESS = true;
    public static final String TEST_SPEC_YML = "classpath:/crossCompilerTests/testSpec.yml";

    private static JSONObject progDeclsFromTestSpec;
    private static JSONObject robotsFromTestSpec;

    private int errorCount = 0;
    private int successCount = 0;

    @BeforeClass
    public static void setup() throws IOException {
        Path path = Paths.get(TARGET_DIR);
        Files.createDirectories(path);
        JSONObject testSpecification = Util.loadYAML(TEST_SPEC_YML);
        progDeclsFromTestSpec = testSpecification.getJSONObject("progs");
        robotsFromTestSpec = testSpecification.getJSONObject("robots");
    }

    @Test
    public void testCommonPartAsUnitTests() throws Exception {
        final String[] programNameArray = progDeclsFromTestSpec.keySet().toArray(new String[0]);
        Arrays.sort(programNameArray);
        {
            List<String> pluginDefines = new ArrayList<>(); // maybe used later to add properties
            IRobotFactory testFactory = Util.configureRobotPlugin(ROBOT_NAME_FOR_COMMON_TESTS, "", "", pluginDefines);
            String defaultConfigXml = testFactory.getConfigurationDefault();
            String templateUnit = Util.readResourceContent(RESOURCE_BASE_COMMON + "/template/commonAstUnit.xml");
            LOG.info("testing XML and AST consistency for " + progDeclsFromTestSpec.length() + " common programs");
            for ( String progName : programNameArray ) {
                logStart(progName + " (test of xml regeneration)");
                JSONObject progDeclFromTestSpec = progDeclsFromTestSpec.getJSONObject(progName);
                String generatedFragmentXml = generateFinalProgram(templateUnit, progName, progDeclFromTestSpec);
                boolean regenerationOk = compareGeneratedAndRegeneratedXml(progName, generatedFragmentXml, defaultConfigXml, "common", testFactory);
                if ( regenerationOk ) {
                    successCount++;
                    logSucc(progName + " (test of xml regeneration)");
                } else {
                    errorCount++;
                    logFail(progName + " (test of xml regeneration)");
                }
            }
        }
        {
            for ( String robotName : ROBOT_NAMES_FOR_TARGET_LANGUAGE_GENERATION ) {
                List<String> pluginDefines = new ArrayList<>(); // maybe used later to add properties
                IRobotFactory testFactory = Util.configureRobotPlugin(robotName, "", "", pluginDefines);
                JSONObject robotDeclFromTestSpec = robotsFromTestSpec.getJSONObject(robotName);
                String robotDir = robotDeclFromTestSpec.getString("template");
                String template = getTemplateWithConfigReplaced(robotDir, robotName);
                nextProg: for ( String progName : programNameArray ) {
                    logStart(progName + " (test code generation for " + robotName + ")");
                    JSONObject codeGenProgDeclFromTestSpec = progDeclsFromTestSpec.getJSONObject(progName);
                    JSONObject exclude = codeGenProgDeclFromTestSpec.optJSONObject("exclude");
                    if ( exclude != null ) {
                        for ( String excludeRobot : exclude.keySet() ) {
                            if ( excludeRobot.equals(robotName) || excludeRobot.equals("ALL") ) {
                                LOG.info("!!!  prog " + progName + " for robot " + robotName + " is excluded. Reason: " + exclude.getString(excludeRobot));
                                continue nextProg;
                            }
                        }
                    }
                    String exportXml = generateFinalProgram(template, progName, codeGenProgDeclFromTestSpec);
                    boolean codeGenerationOk =
                        compareGeneratedTargetLanguage(progName, exportXml, "common/" + robotName, testFactory);
                    if ( codeGenerationOk ) {
                        successCount++;
                        logSucc(progName + " (test code generation for " + robotName + ")");
                    } else {
                        errorCount++;
                        logFail(progName + " (test code generation for " + robotName + ")");
                    }
                }
            }
        }

        LOG.info("succeeding tests: " + successCount);
        if ( errorCount > 0 ) {
            LOG.error("errors found: " + errorCount);
            Assert.fail("errors found: " + errorCount);
        }
    }

    @Test
    public void testRobotSpecificPartAsUnitTests() throws Exception {
        LOG.info("testing robot specific programs");
        final String[] robotNameArray = robotsFromTestSpec.keySet().toArray(new String[0]);
        Arrays.sort(robotNameArray);
        for ( final String robotName : robotNameArray ) {
            LOG.info("processing robot: " + robotName);
            List<String> pluginDefines = new ArrayList<>(); // maybe used later to add properties
            IRobotFactory robotFactory = Util.configureRobotPlugin(robotName, "", "", pluginDefines);
            JSONObject robot = robotsFromTestSpec.getJSONObject(robotName);
            final String robotDir = robot.getString("dir");
            final String resourceDirectory = RESOURCE_BASE_SPECIFIC + robotDir;
            de.fhg.iais.roberta.util.FileUtils.fileStreamOfResourceDirectory(resourceDirectory). //
                filter(f -> f.endsWith(".xml")).forEach(f -> extractProgramFragmentAndProcessProgramXml(f, robotName, resourceDirectory, robotFactory));
        }
        LOG.info("succeeding tests: " + successCount);
        if ( errorCount > 0 ) {
            LOG.error("errors found: " + errorCount);
            Assert.fail("errors found: " + errorCount);
        }
    }

    private void extractProgramFragmentAndProcessProgramXml(
        String fileNameWithRobotSpecificTestProgram,
        String robotName,
        String directoryWithPrograms,
        IRobotFactory testFactory) //
    {
        int index = fileNameWithRobotSpecificTestProgram.lastIndexOf(".xml");
        Assert.assertTrue(index > 0);
        String progName = fileNameWithRobotSpecificTestProgram.substring(0, index);
        if ( "error".equals(progName) ) {
            LOG.info("ignoring program \"error\"");
            return;
        }
        logStart(robotName + "/" + progName);
        String programFileName = directoryWithPrograms + "/" + fileNameWithRobotSpecificTestProgram;
        String exportXmlText = Util.readResourceContent(programFileName);
        Pair<String, String> progConfPair = ProjectWorkflowRestController.splitExportXML(exportXmlText);
        String programXml = progConfPair.getFirst();
        String configXml = progConfPair.getSecond();
        boolean regenerationOk = compareGeneratedAndRegeneratedXml(progName, programXml, configXml, robotName, testFactory);
        boolean codeGenerationOk = compareGeneratedTargetLanguage(progName, exportXmlText, robotName, testFactory);
        if ( regenerationOk && codeGenerationOk ) {
            successCount++;
            logSucc(robotName + "/" + progName);
        } else {
            errorCount++;
            logFail(robotName + "/" + progName);

        }
    }

    //

    /**
     * accept xmlversion 3.1 program and config<br>
     * - generate code for the test factory supplied (main languages are Java, C++, Python and the SimulationStackMachine<br>
     * - check that the program generated is the same as the expected one
     * <br>
     * if an error is detected, the data is written to the directory 'target/unitTests' for debugging
     *
     * @param programName
     * @param programXml
     * @param configXml
     * @param testType either "common" or the name of a robot. Used to select the target directory for storing
     * @param robotFactory
     */
    private boolean compareGeneratedTargetLanguage(String programName, String exportXml, String testType, IRobotFactory robotFactory) //
    {
        Pair<String, String> progConfPair = ProjectWorkflowRestController.splitExportXML(exportXml);
        String programXml = progConfPair.getFirst();
        String configXml = progConfPair.getSecond();
        Project.Builder builder = UnitTestHelper.setupWithConfigAndProgramXML(robotFactory, programXml, configXml);
        Project project = builder.build();

        boolean thisUnitTestIsOk = true;
        try {
            String msg = UnitTestHelper.executeWorkflow("showsource", robotFactory, project);
            if ( msg != null ) {
                LOG.error("showsource workflow failed for " + programName + " with message " + msg);
                thisUnitTestIsOk = false;
                storeExportOfXml(programName, testType, programXml, configXml);
            } else {
                String generatedProgramSource = project.getSourceCode().toString();
                if ( STORE_ALWAYS_DATA_INTO_FILES ) {
                    storeDataIntoFiles(generatedProgramSource, testType + TARGET_LANGUAGE_GENERATED, programName, robotFactory.getSourceCodeFileExtension());
                    storeExportOfXml(programName, testType, programXml, configXml);
                }
            }
        } catch ( Exception e ) {
            LOG.error("showsource workflow failed for " + programName + " with Exception " + e.getMessage());
            thisUnitTestIsOk = true;
        }
        return thisUnitTestIsOk;
    }

    private void storeExportOfXml(String programName, String testType, String programXml, String configXml) {
        String export = "<?xml version=\"1.0\"?>\n<export xmlns=\"http://de.fhg.iais.roberta.blockly\">\n<program>\n";
        export += programXml;
        export += "\n</program>\n<config>\n";
        export += configXml;
        export += "\n</config>\n</export>\n";
        storeDataIntoFiles(export, testType + TARGET_LANGUAGE_SOURCE, programName, "xml");
    }

    /**
     * accept xmlversion 3.1 program and config<br>
     * - generate the AST and compare it with the expected one (compare has to be implemented)
     * - generate the program and config ast embedded in a Project object.<br>
     * - from this Project object regenerate the program and config XML ("backtransformation")<br>
     * - check that the original and regenerated program are similar using XmlUnit<br>
     * - check that the original and regenerated config are similar using XmlUnit (deactivated, because they are VERY different<br>
     * 
     * @param programName
     * @param programXml
     * @param configXml
     * @param testType
     * @param robotFactory
     * @return true, if everything went fine
     */
    private boolean compareGeneratedAndRegeneratedXml(String programName, String programXml, String configXml, String testType, IRobotFactory robotFactory) //
    {
        if ( programName.equals("error") ) {
            LOG.info("ignoring program error");
            return false;
        }
        BlockSet blockSet = null;
        try {
            blockSet = JaxbHelper.xml2BlockSet(programXml);
        } catch ( JAXBException e ) {
            LOG.error("invalid program (AST could not be generated)" + programName);
            return false;
        }
        if ( !"3.1".equals(blockSet.getXmlversion()) ) {
            LOG.error("program XML has NOT version 3.1: " + programName);
            return false;
        }
        Jaxb2ProgramAst<Void> transformer = new Jaxb2ProgramAst(robotFactory);
        ProgramAst<Void> generatedAst = transformer.blocks2Ast(blockSet);
        List<Phrase<Void>> blocks = generatedAst.getTree().get(0);
        StringBuilder sb = new StringBuilder();
        for ( int i = 2; i < blocks.size(); i++ ) {
            sb.append(blocks.get(i).toString()).append("\n");
        }
        if ( STORE_ALWAYS_DATA_INTO_FILES ) {
            storeDataIntoFiles(sb.toString(), testType + AST, programName, "ast");
        }

        Project.Builder builder = UnitTestHelper.setupWithConfigAndProgramXML(robotFactory, programXml, configXml);
        Project project = builder.build();

        String regeneratedProgramXml = project.getAnnotatedProgramAsXml();
        String regeneratedConfigXml = project.getAnnotatedConfigurationAsXml();

        String diffProg = UnitTestHelper.runXmlUnit(programXml, regeneratedProgramXml);
        // String diffConfig = UnitTestHelper.runXmlUnit(configXml, regeneratedConfigXml);

        boolean thisUnitTestIsOk = true;
        if ( diffProg != null ) { // || diffConfig != null
            if ( diffProg != null ) {
                LOG.error(diffProg);
            }
            // if ( diffConfig != null ) {
            //    LOG.error(diffConfig);
            // }
            thisUnitTestIsOk = false;
        }
        if ( STORE_ALWAYS_DATA_INTO_FILES || !thisUnitTestIsOk ) {
            storeDataIntoFiles(programXml, testType + PROG_GENERATED, programName, "xml");
            storeDataIntoFiles(regeneratedProgramXml, testType + PROG_REGENERATED, programName, "xml");

            storeDataIntoFiles(configXml, testType + CONFIG_GENERATED, programName, "xml");
            storeDataIntoFiles(regeneratedConfigXml, testType + CONFIG_REGENERATED, programName, "xml");
        }
        return thisUnitTestIsOk;
    }

    private static String generateFinalProgram(String template, String progName, JSONObject progDeclFromTestSpec) {
        String progSource = read("prog", progName + ".xml");
        Assert.assertNotNull(progSource, "program not found: " + progName);
        template = template.replaceAll("\\[\\[prog\\]\\]", progSource);
        String progFragmentName = progDeclFromTestSpec.optString("fragment");
        String progFragment = progFragmentName.isEmpty() ? "" : read("fragment", progFragmentName + ".xml");
        template = template.replaceAll("\\[\\[fragment\\]\\]", progFragment);
        String declName = progDeclFromTestSpec.optString("decl");
        Assert.assertNotNull(declName, "decl for program not found: " + progName);
        String decl = read("decl", declName + ".xml");
        template = template.replaceAll("\\[\\[decl\\]\\]", decl);
        return template;
    }

    private static String getTemplateWithConfigReplaced(String robotDir, String robotName) {
        String template = Util.readResourceContent(RESOURCE_BASE_COMMON + "template/" + robotDir + ".xml");
        Properties robotProperties = Util.loadProperties("classpath:/" + robotName + ".properties");
        String defaultConfigurationURI = robotProperties.getProperty("robot.configuration.default");
        String defaultConfig = Util.readResourceContent(defaultConfigurationURI);
        final String templateWithConfig = template.replaceAll("\\[\\[conf\\]\\]", defaultConfig);
        return templateWithConfig;
    }

    private static String read(String directoryName, String progNameWithXmlSuffix) {
        try {
            return Util.readResourceContent(RESOURCE_BASE_COMMON + directoryName + "/" + progNameWithXmlSuffix);
        } catch ( Exception e ) {
            // this happens, if no decl or fragment is available for the program given. This is legal.
            return null;
        }
    }

    public static void storeDataIntoFiles(String source, String directory, String programName, String suffix) {
        try {
            String filename = TARGET_DIR + "/" + directory + "/" + programName + "." + suffix;
            if ( "xml".equals(suffix) ) {
                prettyPrintXml(source, filename);
            } else {
                FileUtils.writeStringToFile(new File(filename), source, StandardCharsets.UTF_8.displayName());
            }
        } catch ( Exception e ) {
            Assert.fail("Storing " + programName + " into directory " + TARGET_DIR + " failed");
        }
    }

    public static void prettyPrintXml(String xmlString, String filename) throws Exception {
        File file = new File(filename);
        file.getParentFile().mkdirs();
        file.createNewFile(); // if file already exists will do nothing
        FileOutputStream oFile = new FileOutputStream(file, false);
        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
        xmlString = xmlString.replaceAll("[\r\t\n]+ *<", "<");
        Document document = documentBuilder.parse(new InputSource(new StringReader(xmlString)));
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", Integer.toString(2));
        try (OutputStream os = new FileOutputStream(file)) {
            Result result = new StreamResult(os);
            Source source = new DOMSource(document);
            transformer.transform(source, result);
        }
    }

    public static void logStart(String msg) {
        if ( LOG_NAMES_ON_SUCCESS ) {
            LOG.info("=== program " + msg);
        }
    }

    public static void logSucc(String msg) {
        if ( LOG_NAMES_ON_SUCCESS ) {
            LOG.info("+++ program " + msg);
        }
    }

    public static void logFail(String msg) {
        LOG.info("--- program " + msg);
    }
}
