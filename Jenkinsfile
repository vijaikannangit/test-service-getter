import groovy.json.JsonSlurper

def confluenceBaseUrl = 'https://vijaik.atlassian.net/wiki'
def confluencePageId = '2523141'
def tableIndex = '16'
def tableAppl = 'Applications'
def tableServiceName = 'ServiceName'
def appName = 'RMI Platform'
// def confluenceApiUrl = "${confluenceBaseUrl}/rest/api/content/${confluencePageId}?expand=body.storage"
def confluenceApiUrl = "https://vijaik.atlassian.net/wiki/rest/api/content/2523141?expand=body.storage"
def scriptOutput = '''
{
  "RMI Platform": {
    "RMI Core API": "279",
    "RMI Core UI": "1986",
    "RMI Workflow UI": "1011",
    "RMI Workflow API": "837",
    "RMI Core API-LN": "279",
    "RMI Core UI-LN": "1986"
  }
}
'''

node () {
    stage('Deploy Services') {
        checkout scm
        withCredentials([usernamePassword(credentialsId: 'CONFLUENCE_CRED', usernameVariable: 'CONFLUENCE_USERNAME', passwordVariable: 'CONFLUENCE_APITOKEN')]) {
            // sh "python -m pip install -r requirements.txt --user"
            bat "python -m pip install -r requirements.txt --user"
            bat "python service-getter.py --url '$confluenceApiUrl' --table_index ${appTableIndex} --column_app '$columnApp' --column_service '$columnService' --appname '$appName'"
            def jobsInfo = readJSON file: "jobs.json"
            echo "Service getter output (Map): ${jobsInfo}"
                // Map jobs = [:]
                // for(jobInfo in jobsInfo) {
                //     jobs.put(jobInfo.job, {
                //         stage(jobInfo.job) {
                //             node {
                //                 build(job: jobName, parameters: getJobParamters(jobInfo.parameters), propagate: false)
                //             }
                //         }
                //     })
                // }
                // parallel(jobs)


        }
    }
}

// def getJobParamters(parameters) {
//    def jobParameters = []
//    for (entry in parameters) {
//         jobParameters.add(new StringParameterValue(entry.key, entry.value))
//    }
//    return jobParameters
// }


// def getJobParamters(parameters) {
//    def jobParameters = []
//    for (entry in parameters) {
//         jobParameters.add(new StringParameterValue(entry.key, entry.value))
//    }
//    return jobParameters
// }


// Vijai old Version
// node {
//     stage('Deploy Services') {
//         checkout scm
//         withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USERNAME', passwordVariable: 'CONFLUENCE_APITOKEN')]) {
//             bat "python -m pip install -r requirements.txt --user"
//             echo "Vijai before def "
            
//             // Run Python script and capture the output
//             // def serviceGetterCmd = "python service-getter.py " +
//             //                       "-u '$confluenceApiUrl' " +
//             //                       "-t '$tableIndex' " +
//             //                       "-p '$tableAppl' " +
//             //                       "-s '$tableServiceName' " +
//             //                       "-a \"$appName\""

//             // echo "After service getter"

//             // def servicesInfo = bat(script: serviceGetterCmd, returnStdout: true).trim()
//             // echo "Python script output: ${servicesInfo}"

//             // // Check the exit status
//             // def status = bat(script: serviceGetterCmd, returnStatus: true)
//             // echo "Python script output: ${status}"

//             // if (status == 0) {
//             //     // Print the captured output
//             //     echo "Service getter output (String): ${servicesInfo}"

//             //     // Optionally, convert the output to JSON
//             //     def servicesJson = readJSON text: servicesInfo
//             //     echo "Service getter output (Map): ${servicesJson}"
//             // } else {
//             //     error "Failed to get services list from Confluence page"
//             // }

//             // Execute PYTHON script output
//             script {
//                 // Parse scriptOutput using JsonSlurper
//                 def slurper = new JsonSlurper()
//                 def serviceMap = slurper.parseText(scriptOutput)
//                 echo "ServiceMap: ${serviceMap}"

//                 // Read the content of the JSON file
//                 def jsonFilePath = 'C:/Vijaik/Freelancing/test_service_getter/service-job-mapping.json'
//                 def confDataString = new File(jsonFilePath).text
//                 // Parse JSON content using JsonSlurper
//                 def ConfserviceMap = new JsonSlurper().parseText(confDataString)
//                 echo "ConfserviceMap: ${ConfserviceMap}"

//                 // Execute Service Names
//                 def serviceNamesToExecute = serviceMap['RMI Platform'] 
//                 echo "Here 1"
//                 echo "serviceNamesToExecute: ${serviceNamesToExecute}"

//                 // Map jobs = [:]
//                 // for(serviceName in serviceNamesToExecute) {
//                 //     def serviceConf = ConfserviceMap[serviceName]
//                 //     echo "serviceConf: ${serviceConf}"
//                 //     String jobName = serviceInfo.job
//                 //     String version = seviceNamesToExecute['serviceName']                    
//                 // }
//             }
//         }
//     }
// }


// node () {
//     stage('Deploy Services') {
//         checkout scm
//         withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USERNAME', passwordVariable: 'CONFLUENCE_APITOKEN')]) {
//             bat "python -m pip install -r requirements.txt --user"
//             def serviceGetterCmd = "python service-getter.py -u '$confluenceApiUrl' -t '$tableIndex' -p '$tableAppl' -s '$tableServiceName' -a '$appName'"
//             def status = bat(script: serviceGetterCmd, returnStatus: true)
//             if (status == 0) {
//                 def servicesInfo = readJSON file: "output.json"
//                 echo "Service getter output (Map): ${servicesInfo}"
//             }else {
//                 error "Failed to get services list from confluece page"
//             }
//         }
//     }
// }

                // def slurper = new JsonSlurper()
                // def serviceMap = slurper.parseText(scriptOutput)
                // echo "ServiceMap: ${serviceMap}"

                // println(serviceMap)
                // println "Appliction : ${serviceMap.RMI Platform}"
                // def confDataString = readFile 'service-job-mapping.json'
                // def serviceConfig = slurper.parseText(confDataString)
                // def seviceNamesToExecute = serviceMap['RMI Platform']
                // Map jobs = [:]
                // // for(serviceName in seviceNamesToExecute) {
                // //     def serviceConf = serviceConfig[serviceName]
                // //     String jobName = serviceInfo.job
                // //     String version = seviceNamesToExecute['serviceName']
                // //     // jobs.put(jobName, {
                // //     //     stage(jobName) {
                // //     //         // node {
                // //     //         //     // build(job: jobName, parameters: getJobParamters(serviceConf, version), propagate: false)
                // //     //         // }
                // //     //     }
                // //     // })
                // // }
                // parallel(jobs)


// def getJobParamters(serviceConf, version) {
//     def jobParameters = []
//     Map parameterMap = serviceConf.parameters
//     for (key, val in parameterMap) {
//         String replacedVal = value.value.replace('{{VERSION}}', version)
//         jobParameters.add(new StringParameterValue(key, replacedVal))
//     }
//     return jobParameters
// }