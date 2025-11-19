package org.example.ToolAnnotation

import ai.koog.agents.core.agent.AIAgent
import ai.koog.agents.core.tools.ToolRegistry
import ai.koog.agents.core.tools.reflect.tools
import ai.koog.agents.ext.tool.SayToUser
import ai.koog.prompt.executor.clients.openai.OpenAIModels
import ai.koog.prompt.executor.llms.all.simpleOpenAIExecutor

suspend fun main() {
// 註冊工具集
    val toolRegistry = ToolRegistry {
        tool(SayToUser)
        // 使用 tools 方法註冊
        tools(MathToolSet())
    }

    val agent = AIAgent(
        executor = simpleOpenAIExecutor(System.getenv("OPENAI_API_KEY")),
         systemPrompt = """
             你是一個數學助手。你有一些數學工具可以使用：
             1. 將兩個數字相加 - addNumbers
             2. 將兩個數字相乘 - multiplyNumbers
             3. 檢查數字是否為質數 - isPrime
             當使用者有相關的數學問題時，請選擇相對應的工具來處理和回應
             請用友善的正體中文回應
         """.trimIndent(),
        toolRegistry = toolRegistry,
        llmModel = OpenAIModels.CostOptimized.GPT4_1Mini
    )

    // 測試加法功能
//    agent.run("請幫我計算 25 + 17")
    // 測試乘法功能
    agent.run("請幫我計算 4 x 5 + 八")
    // 測試質數功能
//    agent.run("請問一下 5 是不是質數")
}