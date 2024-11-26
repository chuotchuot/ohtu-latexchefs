function copyToClipboard(elementId) {
    var copyText = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(copyText);
    copyFeedbackMessage("Reference copied to clipboard.");
}

function copyAllReferences(elementId) {
    var allReferencesText = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(allReferencesText);
    copyFeedbackMessage("All references copied to clipboard.");
}

function copyFeedbackMessage(message) {
    const feedback = document.createElement("div");
    feedback.innerText = message;
    feedback.style.position = "fixed";
    feedback.style.bottom = "25px";
    feedback.style.right = "25px";
    feedback.style.backgroundColor = "hsl(256 22 13)";
    feedback.style.color = "white";
    feedback.style.padding = "8px 10px";
    feedback.style.borderRadius = "10px";
    feedback.style.zIndex = "100";
    feedback.style.transition = "opacity 0.3s";

    document.body.appendChild(feedback);

    setTimeout(() => {
        feedback.style.opacity = "0";
        setTimeout(() => feedback.remove(), 300);
    }, 2000);
}