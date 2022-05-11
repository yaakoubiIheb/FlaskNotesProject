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




  function deleteTodo(todoId) {
    fetch("/deleteTodo", {
      method: "POST",
      body: JSON.stringify({ todoId: todoId }),
    }).then((_res) => {
      window.location.href = "/todo";
    });
  }

  function deleteMark(markId) {
    fetch("/deleteMark", {
      method: "POST",
      body: JSON.stringify({ markId: markId }),
    }).then((_res) => {
      window.location.href = "/marks";
    });
  }