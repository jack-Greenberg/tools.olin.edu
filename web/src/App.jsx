import React from "react";
import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";
import { Provider } from "react-redux";

import Router from "./Router";
import store from "./Reducer";
import { login, logout } from "./auth";
import "./App.scss";

const status = {
  UNAUTHORIZED: 401,
  NOT_FOUND: 404,
}

const WHOAMI = gql`
  query getCurrentUser {
    me {
      id
      userId
      displayName
      firstName
    }
  }
`
const App = () => {
  const { loading, error, data } = useQuery(WHOAMI);

  if (error) {
    var { statusCode } = error.networkError;

    switch (statusCode) {
      case status.UNAUTHORIZED:
        store.dispatch(logout());
        break;
      default:
        break;
    }
  } else if (data) {
    store.dispatch(login(data.me));
  }

  if (loading) {
    return <h1>Loading...</h1>;
  }

  return (
    <>
      <Provider store={store}>
        <Router />
      </Provider>
    </>
  )
}

export default App;
