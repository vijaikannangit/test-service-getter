def confluenceBaseUrl = 'https://vijaik.atlassian.net/wiki'
def confluencePageId = '2523141'
def tableIndex = '16'
def tableAppl = 'Applications'
def tableServiceName = 'ServiceName'
def appName = 'RMI Platform'
def confluenceApiUrl = "${confluenceBaseUrl}/rest/api/content/${confluencePageId}?expand=body.storage"

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

node {
    stage('Deploy Services') {
        checkout scm
        withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USERNAME', passwordVariable: 'CONFLUENCE_APITOKEN')]) {
            bat "python -m pip install -r requirements.txt --user"
            echo "Vijai"
            // Run Python script and capture the output
            def serviceGetterCmd = "python service-getter.py -u '$confluenceApiUrl' -t '$tableIndex' -p '$Applications' -s '$ServiceName' -a '$appName'"
            def servicesInfo = bat(script: serviceGetterCmd, returnStdout: true).trim()

            // Check the exit status
            def status = bat(script: serviceGetterCmd, returnStatus: true)

            if (status == 0) {
                // Print the captured output
                echo "Service getter output (String): ${servicesInfo}"

                // Optionally, convert the output to JSON
                def servicesJson = readJSON text: servicesInfo
                echo "Service getter output (Map): ${servicesJson}"
            } else {
                error "Failed to get services list from Confluence page"
            }
        }
    }
}

                // def slurper = new JsonSlurper()
                // def serviceMap = slurper.parseText(scriptOutput)
                // echo "ServiceMap: ${serviceMap}"

                // println(serviceMap)
                // println "Appliction : ${serviceMap.RMI Platform}"
                // println "Age: ${serviceMap.RMI Core API}"
                // println "City: ${serviceMap.RMI Core UI}"
                // println "City: ${serviceMap.RMI Workflow UI}"
                // println "City: ${serviceMap.RMI Workflow API}"
                // println "City: ${serviceMap.RMI Core API-LN}"
                // println "City: ${serviceMap.RMI Core UI-LN}"
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