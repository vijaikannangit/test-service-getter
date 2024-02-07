import groovy.json.JsonSlurper

node {
    def confUrl = 'https://vijaik.atlassian.net/wiki/rest/api/content/33141?expand=body.storage'
    def appName = 'RMI Sample'

    stage('Get Services Info') {
        checkout scm

        withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USERNAME', passwordVariable: 'CONFLUENCE_APITOKEN')]) {
            script {
                def serviceInfoCommand = """
                    python -m pip install -r requirements.txt --user
                    python service-getter.py -u $confUrl -a "$appName"
                    
                """
                // Capture the output of the Python script
                // def scriptOutput = bat(script: serviceInfoCommand, returnStatus: true).trim()
                // Print the output
                echo "Vijai Python Script Output: ${scriptOutput}"
                // def slurper = new JsonSlurper()
                // def serviceMap = slurper.parseText(scriptOutput)
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
            }
        }
    }
}

// def getJobParamters(serviceConf, version) {
//     def jobParameters = []
//     Map parameterMap = serviceConf.parameters
//     for (key, val in parameterMap) {
//         String replacedVal = value.value.replace('{{VERSION}}', version)
//         jobParameters.add(new StringParameterValue(key, replacedVal))
//     }
//     return jobParameters
// }