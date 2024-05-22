const text = "Finalement, la traduction, ça marche!";
console.log("Original text:", text);
fetch("https://t.cxllm.uk/translate", {
	method: "POST",
	body: JSON.stringify({
		q: text,
		source: "auto",
		target: "en",
		format: "text",
		api_key: "fac3533e-1c27-47fa-ab25-4f1b31a1b2f6"
	}),
	headers: { "Content-Type": "application/json" }
}).then((r) => r.json().then(console.log));
