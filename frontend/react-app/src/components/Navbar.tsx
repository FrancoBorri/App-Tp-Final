import { AppBar, Toolbar, Typography, Button, Box } from "@mui/material";
import { useLocation, useNavigate } from "react-router-dom";

const Navbar = () => {
  // Hooks de React Router
  //Permite saber en que ruta estoy
  const location = useLocation();
  // Permite navegar a otra ruta
  const navigate = useNavigate();

  const isActive = (path: string) => {
    // devuelve true si la ruta actual es igual a la que le paso por parametro
    return location.pathname === path;
  };

  return (
    <Box>
      <AppBar position="static">
        <Toolbar>
          <Box
            component="img"
            src="./src/assets/LogoBlanco.svg"
            alt="Logo NeoVentas"
            sx={{ height: 60, mr: 2 }}
          />
          <Typography
            variant="h6"
            component="div"
            sx={{ color: "white", flexGrow: 1, fontWeight: "bold" }}
          >
            NeoVentas
          </Typography>
          <Button
            sx={{
              color: isActive("/inicio") ? "#64B5F6" : "inherit",
            }}
            onClick={() => navigate("/inicio")}
          >
            Inicio
          </Button>
          <Button
            sx={{
              color: isActive("/categorias") ? "#64B5F6" : "inherit",
            }}
            onClick={() => navigate("/categorias")}
          >
            Categorias
          </Button>
          <Button
            sx={{
              color: isActive("/contacto") ? "#64B5F6" : "inherit",
            }}
            onClick={() => navigate("/contacto")}
          >
            Contacto
          </Button>
          <Button
            sx={{
              color: isActive("/login") ? "#64B5F6" : "inherit",
            }}
            onClick={() => navigate("/login")}
          >
            Login
          </Button>
          <Button
            sx={{
              color: isActive("/registro") ? "#64B5F6" : "inherit",
            }}
            onClick={() => navigate("/registro")}
          >
            Registro
          </Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default Navbar;
