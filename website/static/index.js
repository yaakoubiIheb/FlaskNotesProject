function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


  function resetFn(){
    document.getElementById("note").value = ""
    document.getElementById("3ingA").checked = false
    document.getElementById("3ingB").checked = false
    return true
  }