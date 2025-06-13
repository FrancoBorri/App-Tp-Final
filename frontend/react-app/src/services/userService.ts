import axios from "axios";
import type IUser from "../interfaces/IUser";
import type IUserProfile from "../interfaces/IUserProfile";

const API_URL = "http://localhost:8000/api/user";

const UserRegister = async (userData: IUser) => {
  try {
    const response = await axios.post(`${API_URL}/register/`, userData);
    return response.data;
  } catch (error: any) {
    throw error.response?.data || error.message;
  }
};

const userProfileCreate = async (profileData: IUserProfile) => {
  try {
    const response = await axios.post(`${API_URL}/profile/`, profileData);
    return response.data;
  } catch (error: any) {
    throw error.response?.data || error.message;
  }
};

const userProfileUpdate = async (id: number, updateData: IUserProfile) => {
  try {
    const response = await axios.put(`${API_URL}/profile/${id}/`, updateData);
    return response.data;
  } catch (error: any) {
    throw error.response?.data || error.message;
  }
};
export { UserRegister, userProfileCreate, userProfileUpdate };
