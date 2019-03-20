// vim: set syntax=groovy:

node {
    try {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"

        stage 'Test'
            sh 'virtualenv env -p python3.7'
            sh 'source env/bin/activate'
            sh 'env/bin/pip install -r requirements.txt'
            /* NOTE(Richard): Tests here... */
            //sh 'env/bin/python3.7 manage.py test --testrunner=bluereview.tests.(...)'

        stage 'Deploy'
            sh './remote_deploy.sh'

        stage 'Publish results'
            slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
    }
    catch (error) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
        throw error
    }
}
