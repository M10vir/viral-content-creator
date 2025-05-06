export async function fetchAutoPrompt() {
  const response = await fetch("http://localhost:8000/generate-auto-prompt");
  if (!response.ok) {
    throw new Error("Failed to fetch auto prompt");
  }
  const data = await response.json();
  return data.auto_prompt;
}
