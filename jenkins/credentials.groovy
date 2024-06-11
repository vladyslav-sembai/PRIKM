import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.plugins.credentials.*
import jenkins.model.*
import hudson.util.Secret
import org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl

// Функція для отримання змінних середовища
def getEnvVariable(String name) {
    return System.getenv(name)
}

def dockerUserName = getEnvVariable('DOCKERHUB_USERNAME')
def dockerPassword = getEnvVariable('DOCKERHUB_PASSWORD')
def coursBotToken = getEnvVariable('MY_TELEGRAM_BOT_TOKEN')

def newsBotToken = getEnvVariable('NEWS_BOT_TOKEN')

def domain = Domain.global()
def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

def creds = new UsernamePasswordCredentialsImpl(CredentialsScope.GLOBAL, "dockerhub_token", "Description", dockerUserName, dockerPassword)
<<<<<<< HEAD
def coursBotTokenCreds = new StringCredentialsImpl(CredentialsScope.GLOBAL, "cours_tg_bot_token", "Cours TG Bot Token", Secret.fromString(coursBotToken))

store.addCredentials(domain, creds)
store.addCredentials(domain, coursBotTokenCreds)
=======
def newsBotTokenCreds = new StringCredentialsImpl(CredentialsScope.GLOBAL, "news_tg_bot_token", "News TG Bot Token", Secret.fromString(newsBotToken))

store.addCredentials(domain, creds)
store.addCredentials(domain, newsBotTokenCreds)
>>>>>>> 2ace4f5ba933573652589df91ad64ae9bc84d8e4
