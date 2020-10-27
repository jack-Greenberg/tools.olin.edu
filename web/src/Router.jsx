import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Home from "./pages/Home";
import Tools from "./pages/Tools";
import Tool from "./pages/Tool";

import { Header } from "./components";

const AppRouter = () => {
  return (
    <Router>
      <Header />
      <Switch>
        <Route exact path="/" render={() => <Home />} />
        <Route exact path="/tools" render={() => <Tools />} />
        <Route path="/tools/:tool" render={tool => <Tool tool={tool}/>} />
        <Route render={() => (<div>404 :(</div>)} />
      </Switch>
    </Router>
  )
}

export default AppRouter;
