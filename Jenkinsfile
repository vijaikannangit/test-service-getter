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
        withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USERNAME', passwordVariable: 'CONFLUENCE_APITOKEN')]) {
            // sh "python -m pip install -r requirements.txt --user"
            bat "python -m pip install -r requirements.txt --user"
            // bat "python service-getter.py --url '$confluenceApiUrl' --table_index ${appTableIndex} --column_app '$columnApp' --column_service '$columnService' --appname '$appName'"
            def jobsInfo = readJSON file: "jobs.json"
            echo "Service getter output (Map): ${jobsInfo}"
                Map jobs = [:]
                for(jobInfo in jobsInfo) {
                    jobs.put(jobInfo.job, {
                        stage(jobInfo.job) {
                            node {
                                build(job: jobInfo.job, parameters: getJobParamters(jobInfo.parameters), propagate: false)
                            }
                        }
                    })
                }
                parallel(jobs)
        }
    }
}

def getJobParamters(parameters) {
   def jobParameters = []
   for (entry in parameters) {
        jobParameters.add(new StringParameterValue(entry.key, entry.value))
   }
   return jobParameters
}
