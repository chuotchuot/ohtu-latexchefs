function showWarning(warningMessage) {
    const blurOverlay = document.createElement('div');
    blurOverlay.style.position = 'fixed';
    blurOverlay.style.top = '0';
    blurOverlay.style.left = '0';
    blurOverlay.style.width = '100%';
    blurOverlay.style.height = '100%';
    blurOverlay.style.zIndex = '1000';
    blurOverlay.style.backdropFilter = 'blur(5px)';

    const base = document.createElement('div');
    base.style.position = 'fixed';
    base.style.top = '50%';
    base.style.left = '50%';
    base.style.transform = 'translate(-50%, -50%)';
    base.style.backgroundColor = 'rgb(30, 26, 41)';
    base.style.padding = '20px';
    base.style.borderRadius = '10px';
    base.style.textAlign = 'center';
    base.style.zIndex = '1100';

    const warningText = document.createElement('p');
    warningText.textContent = warningMessage;
    warningText.style.marginBottom = '20px';
    warningText.style.fontSize = '16px';
    warningText.style.color = 'white';

    const okButton = document.createElement('button');
    okButton.classList.add("button", "warning")
    okButton.textContent = 'OK';

    okButton.addEventListener('click', () => {
        document.body.removeChild(blurOverlay);
        document.body.removeChild(base);
    });

    base.appendChild(warningText);
    base.appendChild(okButton);
    document.body.appendChild(blurOverlay);
    document.body.appendChild(base);
}

function getReferenceKeys() {
    return fetch('/reference_keys').then(response => {
        return response.json();
    }); 
}