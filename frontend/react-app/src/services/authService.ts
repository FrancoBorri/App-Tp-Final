import axios from "axios";

const API_URL = "http://localhost:8000";

interface LoginData {
  username: string;
  password: string;
}

interface LoginResponse {
  access: string;
  refresh: string;
  user: {
    id: number;
    username: string;
    email: string;
  };
}

const loginService = async (data: LoginData): Promise<LoginResponse> => {
  const response = await axios.post(`${API_URL}/api/user/login/`, data);
  const tokens = response.data;
  const userResponse = await axios.get(`${API_URL}/api/user/`, {
    headers: {
      Authorization: `Bearer ${tokens.access}`,
    },
  });
  return {
    access: tokens.access,
    refresh: tokens.refresh,
    user: userResponse.data,
  };
};

const logout = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("refreshToken");
};

export default {
  loginService,
  logout,
};
