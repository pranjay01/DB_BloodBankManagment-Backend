import React, { Component } from "react";
import { getAllOpeators, deleteOperator } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";

class OperatorList extends Component {
  componentDidMount() {
    this.props.getData();
  }
  deleteBloodBank = (Operator_id) => {
    this.props.deleteOperator(Operator_id, () => {
      this.props.getData();
    });
  };
  render() {
    let { data } = this.props;
    // data = [
    //   { Operator_id: 1, Name: "Salman Mal", Email: "Salmanmal@yahoo.com",Blood_Bank_Name:'Red Cross' },
    //   {
    //     Operator_id: 2,
    //     Name: "Pranjay Sagar",
    //     Email: "prajay.sagar01@gmail.com",
    //     Blood_Bank_Name:'Red Cross'
    //   },
    //   {
    //     Operator_id: 3,
    //     Name: "Apoorv Mehrotra",
    //     Email: "apoorv.mehrotra@sjsu.edu",
    //     Blood_Bank_Name:'Prathma'
    //   },
    // ];
    return (
      <div className="card">
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          List of Operators
          <button
            className="commonbtn"
            style={{ float: "right", marginRight: "10px" }}
            onClick={() => {
              history.push("/AddOperator");
            }}
          >
            Add Operator
          </button>
        </h4>
        <div
          style={{
            textAlign: "left",
            marginLeft: "10px",
            marginRight: "10px",
            borderBottom: "grey solid 1px",
            marginBottom: "5px",
            cursor: "pointer",
          }}
        >
          <div style={{ minWidth: "300px", display: "inline-block" }}>Name</div>
          <div style={{ minWidth: "350px", display: "inline-block" }}>
            Email
          </div>
          <div style={{ minWidth: "300px", display: "inline-block" }}>
            Blood Bank name
          </div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>Edit</div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>
            Delete
          </div>
        </div>
        {data.map((item) => (
          <OperatorRow data={item} delete={this.deleteBloodBank} />
        ))}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.allOperators,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: () => {
      dispatch(getAllOpeators());
    },
    deleteOperator: (Operator_id, callback) => {
      dispatch(deleteOperator(Operator_id, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(OperatorList);

class OperatorRow extends Component {
  delete = () => {
    const { data } = this.props;
    this.props.delete(data.Operator_id);
  };
  render() {
    const { data: item } = this.props;
    return (
      <div
        style={{
          textAlign: "left",
          marginLeft: "10px",
          marginRight: "10px",
          borderBottom: "grey solid 1px",
          marginBottom: "5px",
          cursor: "pointer",
        }}
      >
        <div style={{ minWidth: "300px", display: "inline-block" }}>
          {item.Name}
        </div>
        <div style={{ minWidth: "350px", display: "inline-block" }}>
          {item.Email}
        </div>
        <div style={{ minWidth: "300px", display: "inline-block" }}>
          {item.Blood_Bank_Name}
        </div>
        <div
          style={{ minWidth: "50px", display: "inline-block" }}
          onClick={() => {
            history.push(`/UpdateOperator/${item.Operator_id}`);
          }}
        >
          <a href="#">Edit</a>
        </div>
        <div
          style={{ minWidth: "50px", display: "inline-block" }}
          onClick={this.delete}
        >
          <a href="#">Delete</a>
        </div>
      </div>
    );
  }
}
