import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTask, setNewTask] = useState("");

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = () => {
    fetch('http://localhost:5000/api/todos')
      .then(res => res.json())
      .then(data => setTodos(data))
      .catch(err => console.error("Chyba při stahování dat:", err));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newTask) return;

    fetch('http://localhost:5000/api/todos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ task: newTask })
    })
    .then(res => {
      if (res.ok) {
        setNewTask("");
        fetchTodos();
      }
    });
  };

  const handleDelete = (id) => {
    fetch(`http://localhost:5000/api/todos/${id}`, {
      method: 'DELETE'
    })
    .then(res => {
      if (res.ok) fetchTodos();
    });
  };

  const handleToggle = (id, currentStatus) => {
    fetch(`http://localhost:5000/api/todos/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ done: !currentStatus })
    })
    .then(res => {
      if (res.ok) fetchTodos();
    });
  };

  return (
    <div style={{ padding: "50px", fontFamily: "Arial", maxWidth: "600px", margin: "auto" }}>
      <h1 style={{ textAlign: "center" }}>Docker Todo List 🐳</h1>
      
      <div style={{ background: "#f0f0f0", padding: "20px", borderRadius: "10px" }}>
        <form onSubmit={handleSubmit} style={{ display: "flex", gap: "10px" }}>
          <input 
            type="text" 
            value={newTask} 
            onChange={(e) => setNewTask(e.target.value)} 
            placeholder="Co musím udělat..."
            style={{ flex: 1, padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
          />
          <button type="submit" style={{ padding: "10px 20px", background: "#007bff", color: "white", border: "none", borderRadius: "5px", cursor: "pointer" }}>
            Přidat
          </button>
        </form>
      </div>

      <ul style={{ listStyle: "none", padding: 0, marginTop: "20px" }}>
        {todos.map(todo => (
          <li key={todo.id} style={{ 
            background: "white", 
            borderBottom: "1px solid #eee", 
            padding: "15px", 
            display: "flex", 
            alignItems: "center",
            justifyContent: "space-between",
            boxShadow: "0 2px 5px rgba(0,0,0,0.05)",
            marginBottom: "10px",
            borderRadius: "5px",
            opacity: todo.done ? 0.6 : 1
          }}>
            <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
              <input 
                type="checkbox" 
                checked={todo.done} 
                onChange={() => handleToggle(todo.id, todo.done)}
                style={{ transform: "scale(1.5)", cursor: "pointer" }}
              />
              <span style={{ 
                textDecoration: todo.done ? "line-through" : "none",
                fontSize: "18px"
              }}>
                {todo.task}
              </span>
            </div>
            
            <button 
              onClick={() => handleDelete(todo.id)}
              style={{ 
                background: "#dc3545", 
                color: "white", 
                border: "none", 
                padding: "5px 10px", 
                borderRadius: "3px", 
                cursor: "pointer" 
              }}
            >
              Smazat
            </button>
          </li>
        ))}
      </ul>
      
      {todos.length === 0 && <p style={{ textAlign: "center", color: "#888" }}>Zatím žádné úkoly.</p>}
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));