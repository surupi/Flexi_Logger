plugins {
    id("java")
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(platform("org.junit:junit-bom:5.10.0"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    implementation ("com.fasterxml.jackson.core:jackson-databind:2.15.2") //objectmapper
    implementation ("com.j2html:j2html:1.6.0") //logWithHtmlStyle - tagcreator
}

tasks.test {
    useJUnitPlatform()
}

tasks.register<JavaExec>("runLoggerTest") {
    mainClass.set("LoggerTest")
    classpath = sourceSets["test"].runtimeClasspath
}