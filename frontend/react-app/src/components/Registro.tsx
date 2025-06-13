import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Box, Typography, TextField, Button } from "@mui/material";
import { UserRegister } from "../services/userService";

const registerForm = () => {
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    // Spread operator
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const createUser = async (event: React.FormEvent) => {
    event.preventDefault();
    console.log(
      userData.username + " " + userData.email + " " + userData.password
    );
    try {
      const user = await UserRegister(userData);
      console.log("Usuario registrado", user);
      setUserData({
        username: "",
        email: "",
        password: "",
      });
      navigate("/login");
    } catch (error) {
      console.error("Error al registrar usuario", error);
    }
  };

  return (
    <Box
      maxWidth={500}
      mx="auto"
      mt={5}
      p={3}
      boxShadow={3}
      borderRadius={2}
      component="form"
      onSubmit={createUser}
    >
      <Typography variant="h5" textAlign="center" mb={3}>
        Registro de usuario
      </Typography>
      <TextField
        type="text"
        label="Username"
        name="username"
        value={userData.username} // relaciona el input con el estado
        onChange={handleChange}
        margin="normal"
        autoComplete="username"
        fullWidth
        required
      />
      <TextField
        type="email"
        label="Email"
        name="email"
        value={userData.email}
        onChange={handleChange}
        margin="normal"
        autoComplete="email"
        fullWidth
        required
      />
      <TextField
        type="password"
        label="Password"
        name="password"
        value={userData.password}
        onChange={handleChange}
        margin="normal"
        fullWidth
        required
      />
      <Button
        type="submit"
        variant="contained"
        color="primary"
        fullWidth
        sx={{ mt: 2 }}
      >
        Registrarse
      </Button>
    </Box>
  );
};

export default registerForm;
