package org.example.MCP

import ai.koog.agents.core.agent.AIAgent
import ai.koog.agents.core.tools.ToolRegistry
import ai.koog.agents.ext.tool.AskUser
import ai.koog.agents.mcp.McpToolRegistryProvider
import ai.koog.prompt.executor.clients.openai.OpenAIModels
import ai.koog.prompt.executor.llms.all.simpleOpenAIExecutor
import ai.koog.agents.core.agent.singleRunStrategy

suspend fun main() {

    // 建立整合了 Playwright MCP 工具的 AI Agent
    val executor = simpleOpenAIExecutor(System.getenv("OPENAI_API_KEY"))
    val agent = AIAgent(
        executor = executor,
        strategy = singleRunStrategy(),
        systemPrompt = createPlaywrightSystemPrompt(),
        llmModel = OpenAIModels.CostOptimized.GPT4_1Mini,
        toolRegistry = createPlaywrightToolRegistry()
    )

    val task = """
        打開瀏覽器，幫我到 https://www.tsmc.com/chinese 網站，
        然後到「投資人關係」裡面的「每月營業額報告」的相關頁面，
        然後幫我列出今年最好跟最差月份的營業額跟年度增(減)比率
    """.trimIndent()

    try {
        println("\\n正在執行任務... $task")
        val response = agent.run(task)
        println("\\n回應: $response")
    } catch (e: Exception) {
        println("\\n錯誤: ${e.message}")
    }
}

/**
 * 建立包含 Playwright MCP 工具的註冊表
 */
suspend fun createPlaywrightToolRegistry(): ToolRegistry {
    // 基礎工具
    val basicTools = ToolRegistry {
        tool(AskUser)
    }

    // Playwright MCP 工具
    val playwrightRegistry = createPlaywrightMcpRegistry()

    // 合併工具註冊表
    return basicTools + playwrightRegistry
}

/**
 * Playwright 系統提示詞
 */
fun createPlaywrightSystemPrompt(): String {
    return """
        你是一個專業的網頁自動化助手，具備以下能力：

        1. 使用瀏覽器自動化工具執行網頁操作
        2. 瀏覽指定網站並與頁面元素互動
        3. 擷取網頁內容並分析結果
        4. 執行複雜的多步驟網頁操作流程

        當用戶要求執行網頁相關任務時，請使用 Playwright 工具進行自動化操作
        請確保操作步驟清晰且符合網站的使用條款，而且使用正體中文回答
    """.trimIndent()
}

/**
 * 建立 Playwright MCP 工具註冊表
 */
suspend fun createPlaywrightMcpRegistry(): ToolRegistry {
    val transport = McpToolRegistryProvider.defaultSseTransport("http://localhost:8931/sse")
    return McpToolRegistryProvider.fromTransport(transport)
}