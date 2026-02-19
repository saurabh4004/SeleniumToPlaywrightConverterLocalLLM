const inputArea = document.getElementById('sourceCode');
const outputArea = document.querySelector('#outputCode code');
const convertBtn = document.getElementById('convertBtn');
const statusText = document.getElementById('status');
const filenameInput = document.getElementById('filename');
const filePathDisplay = document.getElementById('filePathDisplay');
const copyBtn = document.getElementById('copyBtn');

convertBtn.addEventListener('click', async () => {
    const sourceCode = inputArea.value.trim();
    if (!sourceCode) {
        alert('Please paste some Java code first.');
        return;
    }

    const outputFilename = filenameInput.value.trim() || 'converted.spec.ts';

    // UI Updates
    convertBtn.disabled = true;
    convertBtn.innerHTML = '<span>⏳ Converting...</span>';
    let startTime = Date.now();
    statusText.textContent = 'Sending to Local LLM (0s elapsed)...';
    outputArea.textContent = '// Conversion in progress... Please wait.';
    filePathDisplay.textContent = '';

    const timerInterval = setInterval(() => {
        const elapsed = Math.floor((Date.now() - startTime) / 1000);
        statusText.textContent = `Processing... (${elapsed}s elapsed). If this is the first run, it may take 1-3 mins.`;
    }, 1000);

    try {
        const response = await fetch('http://localhost:8000/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                source_code: sourceCode,
                output_filename: outputFilename,
                target_language: 'typescript'
            })
        });

        const data = await response.json();

        if (data.success) {
            outputArea.textContent = data.converted_code;
            statusText.textContent = 'Conversion Complete!';
            filePathDisplay.textContent = `Saved to: ${data.file_path}`;
            statusText.style.color = 'var(--success)';
        } else {
            outputArea.textContent = `Error: ${data.message}`;
            statusText.textContent = 'Conversion Failed.';
            statusText.style.color = 'var(--error)';
        }
    } catch (error) {
        console.error(error);
        outputArea.textContent = `Network Error: ${error.message}`;
        statusText.textContent = 'Connection Error.';
        statusText.style.color = 'var(--error)';
    } finally {
        clearInterval(timerInterval);
        convertBtn.disabled = false;
        convertBtn.innerHTML = '<span>⚡ Convert Code</span>';
        setTimeout(() => {
            if (statusText.textContent.includes('Processing')) {
                statusText.style.color = 'var(--text-muted)';
            }
        }, 3000);
    }
});

copyBtn.addEventListener('click', () => {
    const code = outputArea.textContent;
    navigator.clipboard.writeText(code).then(() => {
        const originalText = copyBtn.textContent;
        copyBtn.textContent = 'Copied!';
        setTimeout(() => copyBtn.textContent = originalText, 2000);
    });
});
