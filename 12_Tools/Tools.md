Meta Description:  
Learn how to build, customize, and use tools in LangChain for powerful AI agents. Master built-in and custom tools, toolkits, and their integration with LLMs.

Keywords:  
LangChain tools, custom tools, AI agents, toolkits, LLM integration

Title:  
Mastering LangChain Tools: Build Custom AI Agents with Ease

---

# Mastering LangChain Tools: Build Custom AI Agents with Ease

## Introduction to LangChain Tools and Agents

LangChain is a powerful framework to build AI-powered applications leveraging Large Language Models (LLMs). In this blog post, we explore the crucial concept of **tools** in LangChain and how they enable LLMs to perform real-world tasks. We also delve into building **custom tools**, working with **built-in tools**, and organizing tools into **toolkits** for scalable AI agent development.

### What Are Tools in LangChain?

LLMs have two core capabilities:
- **Reasoning**: The ability to think through and break down questions.
- **Language Generation**: The ability to generate coherent, context-aware text responses.

However, LLMs lack the ability to perform actions such as fetching live data, running code, or interacting with external systems. They are like a human brain that can think and talk but lacks hands and legs to execute tasks.

**Tools** in LangChain act as these “hands and legs” for LLMs. They are functions or APIs that perform specific tasks which LLMs cannot do natively. By connecting tools with an LLM, you empower it to execute actions like booking tickets, searching the web, or interacting with databases.

## Overview of LangChain Tools

### Built-in Tools

LangChain provides a variety of **built-in tools** for common tasks such as:

- **DuckDuckGo Search Tool**: Real-time web search.
- **Wikipedia Query Tool**: Fetch and summarize Wikipedia articles.
- **Python REPL Tool**: Run Python code snippets reliably.
- **Shell Tool**: Execute shell commands on the host system.
- **HTTP Request Tool**: Make HTTP requests.
- **Gmail Send Message Tool**: Send emails via Gmail.
- **Slack Tool**: Interact with Slack channels.
- **SQL Database Query Tool**: Run queries on SQL databases.

These tools are production-ready, require minimal setup, and can be imported and used directly without writing custom code.

### Custom Tools

If your use case requires functionality not covered by built-in tools—such as integrating with your company’s proprietary APIs or custom business logic—you need to create **custom tools**.

Common scenarios for custom tools include:

- Calling your own APIs (e.g., booking systems like MakeMyTrip).
- Encapsulating unique business logic.
- Interacting with internal databases or applications.

Custom tools allow your AI agents to communicate with and control your existing infrastructure.

## How to Create Custom Tools in LangChain

Creating a custom tool in LangChain involves three key steps:

### 1. Define a Python Function

Create a function that contains the logic for the task your tool will perform. For example, a simple multiplication function:

$$
\text{def multiply}(a: \text{int}, b: \text{int}) \to \text{int}:
$$

This function returns the product of two integers $a$ and $b$.

Adding a **docstring** to describe what the function does is highly recommended, as it helps the LLM understand the tool’s purpose.

### 2. Add Type Hinting

Type hinting specifies the input and output data types for your function, helping the LLM know what kind of data to provide and expect back. For example:

$$
a: \text{int}, \quad b: \text{int} \quad \to \quad \text{int}
$$

### 3. Use the `@tool` Decorator

Applying the `@tool` decorator from `langchain.tools` converts your Python function into a special callable that the LLM can interact with. This decorator packs the function with metadata such as the tool name, description, and argument schema.

Example:
$$
@tool
def multiply(a: int, b: int) -> int:
    "Multiply two numbers"
    return a * b
$$

Now, `multiply` becomes a LangChain tool with an `invoke` method that accepts inputs and returns results.

---

## Exploring Built-in Tools with Examples

### Example: DuckDuckGo Search Tool

Imagine you want your AI agent to fetch the latest news. Since LLMs have a knowledge cut-off date and cannot perform live searches, the DuckDuckGo search tool bridges this gap.

To use it:

1. Import the tool from `langchain.community.tools`.
2. Create an instance.
3. Call the tool’s `invoke` method with the search query.

The tool sends the query to DuckDuckGo, fetches results, and returns them to the LLM for response generation.

### Example: Shell Tool

This tool allows running shell commands on the host machine where the LangChain agent is running. It is useful for interacting with files or system processes.

**Warning:** Use this tool cautiously, especially in production, as it can execute destructive commands.

---

## Advanced Custom Tools: Structuring with Pydantic and BaseTool

LangChain supports multiple ways to create custom tools with increasing levels of structure and customization.

### Method 1: Using `@tool` Decorator (Simple)

- Quick and easy for prototyping.
- Less strict input validation.
- Suitable for most use cases.

### Method 2: Structured Tools with Pydantic

- Define a Pydantic model to enforce strict input schema.
- Create a tool using `StructuredTool.from_function`.
- Provides better validation and documentation.
- Recommended for production-ready tools.

Example:

Define input schema:

$$
\text{class MultiplyInput(BaseModel):} \\
\quad a: int \\
\quad b: int
$$

Create the tool:

$$
\text{tool} = StructuredTool.from_function(
    multiply,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)
$$

### Method 3: Extending the `BaseTool` Class

- Full control over tool behavior.
- Define name, description, argument schema as class attributes.
- Implement a `run` method to execute logic.
- Supports advanced features like asynchronous execution.
- Ideal for complex or highly customized tools.

Example:

```python
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(..., description="First number")
    b: int = Field(..., description="Second number")

class MultiplyTool(BaseTool):
    name = "Multiply"
    description = "Multiply two numbers"

    args_schema = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b
```

---

## Toolkits in LangChain: Organizing Related Tools

When your application requires multiple related tools, you can group them into a **toolkit**. This offers convenience, reusability, and better management.

### What is a Toolkit?

A toolkit is a collection of related tools packaged together serving a common purpose.

For example, a **Google Drive Toolkit** might include:

- Upload file tool.
- Search files tool.
- Read file tool.

LangChain supports both built-in toolkits and custom toolkits created by users.

### Creating a Custom Toolkit

To create a custom toolkit:

1. Define multiple related tools.
2. Create a class with a `get_tools` method returning the list of tools.

Example:

```python
class MathToolkit:
    def get_tools(self):
        return [add_tool, multiply_tool]
```

You can then instantiate the toolkit and access all tools at once, facilitating easy integration with your AI agent.

---

## Connecting Tools with LLMs: The Role of Tool Calling

Tools by themselves perform tasks, but the magic happens when they are connected to LLMs via **tool calling**:

- The LLM decides **when** and **which tool** to call based on the conversation.
- It formats inputs, calls the tool, and processes the output.
- This interaction enables building autonomous AI agents capable of multi-step reasoning and actions.

Tool calling is a critical next step covered in detail in subsequent LangChain tutorials.

---

## Conclusion

In this extensive guide, we covered:

- The concept and importance of **tools** in LangChain.
- How **built-in tools** provide ready-made solutions for common tasks.
- How to **create custom tools** using three different methods with Python functions, Pydantic models, and BaseTool classes.
- How to organize tools into **toolkits** for modular and reusable AI systems.
- The fundamental relationship between LLMs and tools that powers autonomous AI agents.

Understanding and mastering tools in LangChain is crucial for developing AI agents that go beyond text generation to perform real-world tasks autonomously. Whether you want to use built-in tools or build fully customized solutions, LangChain provides a flexible and powerful toolkit to help you achieve that.

---

## FAQs

**Q1: Why do LLMs need tools?**  
LLMs can think and generate language but cannot execute tasks like booking tickets or running code. Tools extend their capabilities by performing those tasks.

**Q2: What is the simplest way to create a custom tool?**  
Using the `@tool` decorator on a Python function is the simplest and most common method.

**Q3: When should I use structured tools with Pydantic?**  
For production-grade applications where strict input validation and schema enforcement are needed.

**Q4: How do toolkits help in LangChain?**  
Toolkits group related tools together for convenience, reusability, and better management in complex applications.

---

Embrace the power of LangChain tools to build intelligent AI agents that can think, act, and solve complex problems with seamless integration into your applications. Stay tuned for upcoming tutorials on tool calling and agent building!

--

Meta Description:  
Learn how to create and connect AI tools with Large Language Models (LLMs) for real-time tasks like currency conversion using LangChain.

Keywords:  
LLM tool binding, LangChain tutorial, AI tool calling, real-time currency conversion

Title:  
Mastering LLM Tool Binding and Calling with LangChain

---

# Mastering LLM Tool Binding and Calling with LangChain

## Introduction to LangChain and AI Tools

Large Language Models (LLMs) are powerful AI systems capable of **reasoning** and **generating outputs** based on input queries. However, they cannot perform actual tasks such as querying databases, executing commands, or hitting external APIs on their own. To overcome these limitations, the concept of **tools** is introduced.

Tools are specialized functions or APIs that LLMs can be connected to, enabling the AI to carry out various operations by "calling" these tools during conversations. This blog post explains the core concepts of creating tools, binding them to LLMs, calling them during interactions, and executing them practically using LangChain — a popular framework for building AI applications.

---

## Core Concepts of LLMs and Tools

### Understanding LLMs' Capabilities and Limitations

LLMs are like humans who can **think** (reason) and **speak** (generate text), but lack physical abilities (hands and feet) to perform tasks. For example:

- LLMs can understand complex queries by breaking them down.
- They generate relevant textual responses.
- But they **cannot** directly perform actions like updating a database, posting on social media, or fetching real-time data from APIs.

### The Role of Tools in AI Applications

To empower LLMs to perform tasks, we use **tools** — essentially Python functions or external APIs explicitly designed to execute specific jobs, like searching the web or performing calculations.

- **Built-in tools:** Predefined by the framework or platform.
- **Custom tools:** Created by developers to suit specific needs.

Tools can interact with LLMs by receiving structured inputs and providing outputs, allowing the LLM to delegate tasks it cannot perform natively.

---

## Step 1: Tool Creation

Creating a tool involves defining a function that performs a well-scoped task. For example, a simple multiplication tool can be implemented as:

$$
\text{multiply}(A, B) = A \times B
$$

The tool must include:

- **Name:** Identifies the tool.
- **Description:** Explains the tool’s purpose to the LLM.
- **Input schema:** Defines the format and type of inputs the tool accepts.
- **Output:** Specifies what the tool returns.

```python
@tool
def multiply(A: int, B: int) -> int:
    "Given two numbers A and B, returns their product."
    return A * B
```

---

## Step 2: Tool Binding to LLM

**Tool binding** is the process of registering tools with the LLM, so the model knows which tools are available, what they do, and how to use them.

- This involves providing the tool’s name, description, and input format to the LLM.
- The LLM can then decide during conversations whether to use a particular tool.

Example of binding a single tool:

```python
llm = ChatOpenAI()
llm_with_tools = llm.bind_tools([multiply])
```

Multiple tools can be bound simultaneously by passing a list.

---

## Step 3: Tool Calling

Tool calling is when the LLM decides to invoke a tool during a conversation. This happens when:

- The LLM recognizes the user's query requires a function beyond text generation.
- It generates a **structured output** indicating which tool to call and with what arguments.

For example, a query "What is 8 * 7?" prompts the LLM to respond with:

```json
{
  "tool_call": {
    "name": "multiply",
    "arguments": {"A": 8, "B": 7}
  }
}
```

**Important:** The LLM does **not** execute the tool itself but suggests the tool call and arguments.

---

## Step 4: Tool Execution

The actual execution of the tool is done by the developer’s program or framework:

- The program receives the LLM’s suggestion.
- It invokes the specified tool with the provided arguments.
- The tool runs, and the output is returned.
- This output can be encapsulated in a **tool message** and sent back to the LLM for final response generation.

Example workflow:

1. LLM suggests calling `multiply` with $A=8$, $B=7$.
2. Program runs `multiply(8, 7)` and gets $56$.
3. Program sends back the result to LLM.
4. LLM generates a final answer: "The product of 8 and 7 is 56."

---

## Practical Example: Real-Time Currency Conversion Application

### Problem Statement

Currency conversion rates fluctuate constantly. LLMs possess historic data but lack **real-time** exchange rates. Our goal is to build an application where:

- The LLM can fetch current exchange rates.
- Perform currency conversions using those rates.
- Answer user queries like: *"Convert 80 USD to INR."*

### Solution Outline

We solve this with two tools:

1. **Get Conversion Factor Tool:**

   - Hits an exchange rate API.
   - Returns the current conversion rate between two currencies.

2. **Convert Currency Tool:**

   - Takes a base currency amount and conversion factor.
   - Returns the converted currency value.

---

### Tool 1: Get Conversion Factor Tool

- **Inputs:** Base currency code (string), Target currency code (string).
- **Output:** Conversion rate (float).

This tool uses an external API to fetch the latest exchange rate.

```python
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    Fetches the currency conversion factor between base_currency and target_currency.
    """
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}&apikey=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]
```

---

### Tool 2: Convert Currency Tool

- **Inputs:** Base currency value (int), Conversion rate (float).
- **Output:** Converted value (float).

```python
@tool
def convert_currency(base_value: int, conversion_rate: float) -> float:
    """
    Calculates target currency value from base_value using conversion_rate.
    """
    return base_value * conversion_rate
```

---

### Binding Tools to LLM

Both tools are bound to the LLM:

```python
llm_with_tools = llm.bind_tools([get_conversion_factor, convert_currency])
```

---

### Tool Calling and Execution Workflow

1. User query: *"What is the conversion factor between USD and INR and convert 10 USD to INR?"*
2. LLM generates two tool calls:
   - Call `get_conversion_factor` with `base_currency="USD"`, `target_currency="INR"`.
   - Call `convert_currency` with `base_value=10`, `conversion_rate=<value from first tool>`.
3. Developer program executes tool 1, retrieves the conversion rate.
4. Injects this conversion rate as an argument for tool 2.
5. Executes tool 2 to get the final converted amount.
6. Sends all messages (human, AI, tool calls, tool results) back to LLM for final response generation.
7. LLM outputs the answer with accurate real-time conversion.

---

## Handling Dependency Between Tools: Injected Tool Arguments

Sometimes, one tool’s output is needed as input for another. For example, the conversion rate fetched by the first tool must be injected into the second tool’s call.

To handle this:

- Mark the dependent argument as **injected** so LLM does not fill it during tool calling.
- Developer program fills this argument manually after the first tool executes.

Example:

```python
from langchain.tools import InjectedToolArgument
from typing import Annotated

@tool
def convert_currency(
    base_value: int,
    conversion_rate: Annotated[float, InjectedToolArgument()]
) -> float:
    return base_value * conversion_rate
```

This ensures clean handling of sequential tool execution with data dependencies.

---

## Maintaining Conversation History and Context

To enable coherent conversations, maintain a **message history** list:

- Human messages
- AI messages
- Tool call messages
- Tool execution results

Each cycle appends new messages, preserving the full context for the LLM to generate informed responses.

Example:

```python
messages = [HumanMessage(content=user_query)]
ai_response = llm_with_tools.invoke(messages)
messages.append(ai_response)

# Extract tool calls, execute tools, append tool messages
messages.append(tool_message)

# Resend full messages for final answer
final_response = llm_with_tools.invoke(messages)
```

---

## Summary: Four Key Steps for LLM-Tool Integration

| Step             | Description                                                   |
|------------------|---------------------------------------------------------------|
| **Tool Creation** | Define Python functions with input/output schemas and descriptions. |
| **Tool Binding**  | Register tools with LLM so it recognizes available tools and their specs. |
| **Tool Calling**  | LLM decides which tool to call and generates structured arguments. |
| **Tool Execution**| Developer executes the tool with given inputs and returns results to LLM. |

---

## Conclusion and Next Steps

This tutorial covered fundamental concepts of integrating tools with LLMs using LangChain, including:

- Creating custom tools for tasks like multiplication and currency conversion.
- Binding tools with LLMs.
- Understanding how LLMs suggest tool calls without executing them.
- Executing tools programmatically and feeding results back to LLM.
- Managing tool argument injection for dependent tool workflows.
- Maintaining conversation context for coherent multi-step interactions.

The final currency conversion application demonstrated a real-world use case, showcasing how LLMs can be augmented with external tools to provide **real-time, actionable intelligence**.

### Looking Ahead: Building Autonomous AI Agents

The current approach requires manual orchestration of tool executions by the developer. The next frontier is building **autonomous AI agents** that:

- Break down problems independently.
- Manage calling and executing tools themselves.
- Operate without manual intervention.

Future tutorials will dive into building such agents with LangChain.

---

## Frequently Asked Questions (FAQ)

### 1. Can LLMs execute tools by themselves?  
No, LLMs only suggest tool calls with arguments. Actual execution is done by the developer or the framework.

### 2. What is tool binding?  
It is the registration of tools with the LLM, informing it about available tools, their functionality, and input requirements.

### 3. How does tool calling differ from tool execution?  
Tool calling is the LLM deciding which tool to invoke and providing arguments. Tool execution is running the tool with those arguments to get results.

### 4. How to handle dependent tool calls?  
Use **injected tool arguments** to manually fill inputs for tools that depend on outputs of previously executed tools.

---

Harnessing tool binding and calling with LangChain unlocks the true potential of LLMs by giving them the ability to perform real-world tasks beyond text generation. This modular approach allows you to build scalable, intelligent applications capable of integrating external APIs, databases, and services seamlessly.