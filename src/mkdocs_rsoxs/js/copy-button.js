const codeBlockSelectors = ["div.highlight", "div.codehilite"];
for (const block of document.querySelectorAll(codeBlockSelectors.join(", "))) {
	if (!block.querySelector("code") || block.querySelector("button.code-copy-button")) {
		continue;
	}
	if (!block.classList.contains("codehilite")) {
		block.classList.add("codehilite");
	}
	const button = document.createElement("button");
	button.setAttribute("type", "button");
	button.setAttribute("class", "code-copy-button");
	button.setAttribute("aria-label", "Copy code block");

	const span = document.createElement("span");
	span.setAttribute("class", "sr-only");
	span.innerText = "Copy";
	button.appendChild(span);

	const icon = clipboardIcon();
	button.appendChild(icon);
	button.onclick = onCodeCopy;
	block.appendChild(button);
}
