import React from "react";
import { useSelector } from "react-redux";
import styled from "styled-components";
import { Link } from "react-router-dom";

import { ReactComponent as ShopLogo } from "../../images/logo.svg";

const StyledHeader = styled.header`
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
`

const HeaderLeft = styled.div`
`

const StyledHeadline = styled.p`
  display: flex;
  align-items: center;
  margin-bottom: -1em;

  & svg {
    width: 30%;
    margin-right: .5em;
  }
  & .title {
    font-size: 2em;
    font-family: 'din-2014', sans-serif;
    font-weight: bold;
    color: black;
    text-decoration: none;
  }
`
const StyledSubtitle = styled.p`
  font-size: 1.25em;
  font-family: 'din-2014', sans-serif;
  margin-left: 1em;
`

const Header = (props) => {
  const auth = useSelector(state => state.auth);

  return (
    <StyledHeader>
      <HeaderLeft>
        <StyledHeadline>
          <ShopLogo width="300px" />
          <Link class="title" to="/">Tools.Olin</Link>
        </StyledHeadline>

        <StyledSubtitle>
          Machine shop trainings.
        </StyledSubtitle>

      </HeaderLeft>
      <div>
        <Nav auth={auth} />
      </div>
    </StyledHeader>
  )
}

const StyledNav = styled.nav`
  display: flex;
  flex-direction: column;
  align-items: end;
  justify-content: flex-end;
`

const Nav = (props) => {
  const { auth } = props;

  return (
    <StyledNav>
      <AuthHeader auth={auth} />
      <ul>
        <Link to="/tools">Tools</Link>
      </ul>
    </StyledNav>
  )
}

const ButtonLink = styled.a`
  font-size: 1em;
  font-family: 'din-2014', sans-serif;
  border: 1px solid black;
  color: inherit;
  text-decoration: none;

  display: inline;
  padding: .2em .3em;
`

const AuthHeader = (props) => {
  const { auth } = props;

  return (
    <div style={{marginBottom: '1em'}}>
      {
        auth.isAuthenticated
          ? (
            <div style={{fontSize: '1em', fontFamily: 'din-2014, sans-serif'}}>
              Welcome, {auth.user.firstName}! <ButtonLink href="/auth/logout">Logout</ButtonLink>
            </div>
          ) : (
            <ButtonLink href="/auth/login">Login</ButtonLink>
          )
      }
    </div>
  )
}

export default Header;
