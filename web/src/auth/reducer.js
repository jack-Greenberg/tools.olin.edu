import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  isAuthenticated: false,
  user: {
    id: undefined,
    firstName: undefined,
    lastName: undefined,
    displayName: undefined,
    email: undefined,
  }
}

export const authSlice = createSlice({
  name: "authentication",
  initialState,
  reducers: {
    logout(state) {
      state = initialState;
    },
    login(state, action) {
      state.isAuthenticated = true;
      state.user = action.payload;
    }
  }
})

export const { logout, login } = authSlice.actions;
export default authSlice.reducer;
