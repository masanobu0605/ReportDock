function removeSpaces() {
    let text = document.getElementById('text-input').value;
    fetch('/remove_spaces', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text: text})
    })
    .then(response => response.json())
    .then(data => displayResult(data.result));
}

function replaceText() {
    let inputtext = document.getElementById('input_text_replace').value;
    let oldText = document.getElementById('old_text').value;
    let newText = document.getElementById('new_text').value;

    fetch('/replace_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text: inputtext, old: oldText, new: newText})
    })
    .then(response => response.json())
    .then(data => displayResult(data.result))
    .catch(error => console.error('Error:', error));
}



function countCharacters() {
    let text = document.getElementById('text-input').value;
    fetch('/count_characters', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text: text})
    })
    .then(response => response.json())
    .then(data => displayResult('文字数 : ' + data.count));
}

function displayResult(result) {
    const resultContainer = document.getElementById('result');
    resultContainer.textContent = result;  // 処理結果をテキストとして表示
}

// 要約機能の実装予定がない場合は以下の関数を削除
// function summarizeText() {
//     let text = document.getElementById('text-input').value;
//     // 要約機能の実装が必要
//     let result = "要約機能はまだ実装されていません"; // 仮の実装
//     displayResult(result);
// }


function copyText() {
    const outputText = document.getElementById('result');
    if (outputText) {
        navigator.clipboard.writeText(outputText.value)
            .then(() => {
                console.log('Text copied to clipboard successfully!');
            })
            .catch(err => {
                console.error('Failed to copy text: ', err);
            });
    } else {
        console.error('Output textarea not found');
    }
}
