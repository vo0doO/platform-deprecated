import React from "react";
import ReactDOM from "react-dom";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbreact/dist/css/mdb.css";
import "./index.css";
import ModalForm from "./ModalForm";

import registerServiceWorker from "./registerServiceWorker";

ReactDOM.render(<ModalForm />, document.getElementById("ModalForm"));

registerServiceWorker();
