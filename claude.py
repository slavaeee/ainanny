# 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
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message.content)
