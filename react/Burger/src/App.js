import React, { useContext, useState } from "react";
import "./App.css";
import Data from "./data.js";
import Detail from "./Detail.js";
import Cart from "./Cart.js";
import { Link, Route, Switch, useHistory } from "react-router-dom";
import { Navbar, Container, Nav, NavDropdown } from "react-bootstrap";
import axios from "axios";
import SimpleImageSlider from "./slider/slider.js";
export let 재고context = React.createContext();

function App() {
  let [shoes, shoes변경] = useState(Data);
  let [재고, 재고변경] = useState([10, 11, 12]);
  return (
    <div className="App">
      <Menu></Menu>
      <Switch>
        <Route exact path="/">
          <SimpleImageSlider />

          <div className="container">
            <재고context.Provider value={재고}>
              <div className="row">
                {shoes.map((a, i) => {
                  return <Shoes shoes={shoes[i]} i={i} key={i}></Shoes>;
                })}
              </div>
            </재고context.Provider>
            <button
              className="btn btn-primary"
              onClick={() => {
                axios
                  .get("https://codingapple1.github.io/shop/data2.json")
                  .then((result) => {
                    console.log(result.data);
                    shoes변경([...shoes, ...result.data]);
                  })
                  .catch(() => {
                    alert("실패");
                  });
              }}
            >
              더보기
            </button>
          </div>
        </Route>
        <Route path="/detail/:id">
          <재고context.Provider value={재고}>
            <Detail shoes={shoes} 재고={재고} 재고변경={재고변경}></Detail>
          </재고context.Provider>
        </Route>
        <Route path="/cart">
          <Cart></Cart>
        </Route>

        <Route path="/:id">
          <div>아무거나</div>
        </Route>
      </Switch>
    </div>
  );
}

function Shoes(props) {
  let 재고 = useContext(재고context);
  let history = useHistory();

  return (
    <div
      className="col-md-4"
      onClick={() => {
        history.push("/detail/" + props.shoes.id);
      }}
    >
      <img
        src={
          "https://codingapple1.github.io/shop/shoes" + (props.i + 1) + ".jpg"
        }
        width="100%"
      />
      <h4>{props.shoes.title}</h4>
      <p>
        {props.shoes.content} & {props.shoes.price}
      </p>
      <Test></Test>
    </div>
  );
}
function Test() {
  let 재고 = useContext(재고context);
  return <p>재고:{재고[0]}</p>;
}

function Menu() {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="/">Lee Shop</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link>
              <Link to="/">Home</Link>
            </Nav.Link>
            <Nav.Link>
              <Link to="/Detail">Detail</Link>
            </Nav.Link>
            <NavDropdown title="Shop" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">McDonald's</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">
                Burger King
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Lotteria</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.4">
                Mom's Touch
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.5">KFC</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default App;
