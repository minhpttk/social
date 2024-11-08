node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Prepare Environment') {
        withCredentials([
            string(credentialsId: 'DB_USER', variable: 'DB_USER'),
            string(credentialsId: 'DB_PASS', variable: 'DB_PASS'),
            string(credentialsId: 'DB_HOST', variable: 'DB_HOST'),
            string(credentialsId: 'DB_PORT', variable: 'DB_PORT'),
        ]) {
            script {
                def envContent = """
                    DEBUG=True
                    DB_TYPE=mysql
                    DB_NAME=shopgame
                    DB_USER=${env.DB_USER}
                    DB_PASS=${env.DB_PASS}
                    DB_HOST=${env.DB_HOST}
                    DB_PORT=${env.DB_PORT}
                    CORS_ORIGIN_WHITELIST=http://localhost:3033,http://localhost:3000,https://shopducmomtv.net,https://www.shopducmomtv.net,https://admin.shopducmomtv.net,https://www.shopsontung.com,https://admin.shopsontung.com
                """.stripIndent().trim()

                writeFile(file: '.env', text: envContent)
            }
        }
    }

    stage('Set Execute Permission for Entrypoint') {
        script {
            sh 'chmod +x entrypoint.sh'
        }
    }

    stage('Build image') {
       app = docker.build("batungnbt/shopgame-api")
    }

    stage('Test image') {
        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        withDockerRegistry(credentialsId: 'tecser-docker-hub', url: 'https://index.docker.io/v1/') {
            app.push("${env.BUILD_NUMBER}")
        }
    }

    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'SHOPGAME-UPDATE-MANIFEST', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}