import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/Navbar";
import Categorías from "./components/Categorias";
import Contacto from "./components/Contacto";
import Inicio from "./components/Inicio";
import Login from "./components/Login";
import Registro from "./components/Registro";
function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/inicio" element={<Inicio />} />
        <Route path="/categorias" element={<Categorías />} />
        <Route path="/contacto" element={<Contacto />} />
        <Route path="/login" element={<Login />} />
        <Route path="/registro" element={<Registro />} />
      </Routes>
    </Router>
  );
}

export default App;
