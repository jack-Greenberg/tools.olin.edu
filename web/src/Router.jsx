import React, { Component } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Home from "./pages/Home";
// import Login from "./pages/Login";

class AppRouter extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" render={() => <Home />} />
          <Route render={() => (<div>404 :(</div>)} />
        </Switch>
      </Router>
    );
  }
}

export default AppRouter;
