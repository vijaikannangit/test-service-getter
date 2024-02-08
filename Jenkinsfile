def confluenceBaseUrl = 'https://vijaik.atlassian.net/wiki'
def confluencePageId = '33141'
def appName = 'RMI Platform'
def confluenceApiUrl = "${confluenceBaseUrl}/rest/api/content/${confluencePageId}?expand=body.storage"

node () {
    stage('Deploy Services') {
        checkout scm
        withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USERNAME', passwordVariable: 'CONFLUENCE_APITOKEN')]) {
            sh "python -m pip install -r requirements.txt --user"
            def serviceGetterCmd = "python service-getter.py --url '$confluenceApiUrl' --appname '$appName'"
            def status = sh(script: serviceGetterCmd, returnStatus: true)
            if (status == 0) {
                def servicesInfo = readJSON file: "output.json"
                echo "Service getter output (Map): ${servicesInfo}"
            }else {
                error "Failed to get services list from confluece page"
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