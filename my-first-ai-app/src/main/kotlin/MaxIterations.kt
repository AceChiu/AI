package org.example

import ai.koog.agents.core.agent.AIAgent
import ai.koog.agents.core.tools.ToolRegistry
import ai.koog.agents.ext.tool.SayToUser
import ai.koog.agents.ext.tool.AskUser
import ai.koog.agents.ext.tool.ExitTool
import ai.koog.prompt.executor.clients.openai.OpenAIModels
import ai.koog.prompt.executor.llms.all.simpleOpenAIExecutor

suspend fun main() {
       val toolRegistry = ToolRegistry {
        tool(SayToUser)
    }

    // 設定較少的迭代次數 - 適合簡單任務
    val quickAgent = AIAgent(
        executor = simpleOpenAIExecutor(System.getenv("OPENAI_API_KEY")),
        systemPrompt = """
            你是一個快速回應助手。收到問題後，直接給出簡潔的答案，
            不需要過度思考或使用工具。
        """.trimIndent(),
        toolRegistry = toolRegistry,
        maxIterations = 30, // 最多 30 個步驟
        llmModel = OpenAIModels.CostOptimized.GPT4_1Mini
    )

    // 設定較多的迭代次數 - 適合需要深度思考的任務
    val thoughtfulAgent = AIAgent(
        executor = simpleOpenAIExecutor(System.getenv("OPENAI_API_KEY")),
        systemPrompt = """
            你是一個深思熟慮的助手。對於複雜問題，你會：
            1. 先用 SayToUser 說明你的思考過程
            2. 分析問題的不同面向
            3. 最後提供完整的建議
        """.trimIndent(),
        toolRegistry = toolRegistry,
        maxIterations = 100, // 允許更多思考步驟
        llmModel = OpenAIModels.CostOptimized.GPT4_1Mini
    )

    val question = "如何提升工作效率？"

    println("=== ⚡ 快速回應模式 (MaxIterations: 30) ===")
    quickAgent.run(question)

    println("\n=== 🤔 深度思考模式 (MaxIterations: 100) ===")
    thoughtfulAgent.run(question)
}