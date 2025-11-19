package org.example.MultiLLM

object ApiKeyManager {
    val openAIApiKey: String = System.getenv("OPENAI_API_KEY")
    val googleApiKey: String = System.getenv("GOOGLE_API_KEY")
    val ollamaBaseUrl: String = System.getenv("OLLAMA_BASE_URL")

    // 檢查可用的供應商
    fun getAvailableProviders(): List<String> {
        val available = mutableListOf<String>()

        if (openAIApiKey.isNotBlank()) {
            available.add("OpenAI")
        }

        if (googleApiKey.isNotBlank()) {
            available.add("Google")
        }

        if (ollamaBaseUrl.isNotBlank()) {
            available.add("Ollama")
        }

        return available
    }
}