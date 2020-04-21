import React, { Component } from "react";
import { getAllBloodBankInfo, deleteBloodBank } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";
class BloodBankList extends Component {
  componentDidMount() {
    this.props.getData();
  }
  deleteBloodBank = (Bbank_id) => {
    this.props.deleteBloodBank(Bbank_id, () => {
      this.props.getData();
    });
  };
  render() {
    let { data } = this.props;
    // data = [
    //   { Bbank_id: 1, Name: "Red Cross", Type: "Main", Phone_no: 6692819690 },
    //   { Bbank_id: 2, Name: "Prathma", Type: "Main", Phone_no: 6692819690 },
    //   { Bbank_id: 3, Name: "Salman", Type: "Main", Phone_no: 6692819690 },
    // ];
    return (
      <div className="card">
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          List of Blood Banks

          <button
            className="commonbtn"
            style={{ float: "right", marginRight: "10px" }}
            onClick={()=>{history.push('/AddBloodBank')}}
          >
            Add Blood Bank
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
          <div style={{ minWidth: "300px", display: "inline-block" }}>
            Blood Bank Name
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>Type</div>
          <div style={{ minWidth: "150px", display: "inline-block" }}>
            Phone No
          </div>
          <div style={{ minWidth: "50px", display: "inline-block" }} >Edit</div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>
            Delete
          </div>
        </div>
        {data&&data.map((item) => (
          <BloodBankRow data={item} delete={this.deleteBloodBank} />
        ))}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.bloodBankList,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: () => {
      dispatch(getAllBloodBankInfo());
    },
    deleteBloodBank: (Bbank_id, callback) => {
      dispatch(deleteBloodBank(Bbank_id, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(BloodBankList);

class BloodBankRow extends Component {
  delete = () => {
    const { data } = this.props;
    this.props.delete(data.Bbank_id);
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
        <div style={{ minWidth: "200px", display: "inline-block" }}>
          {item.Type}
        </div>
        <div style={{ minWidth: "150px", display: "inline-block" }}>
          {item.Phone_no}
        </div>
        <div
          style={{ minWidth: "50px", display: "inline-block" }}
          onClick={() => {
            history.push(`/UpdateBloodBank/${item.Bbank_id}`);
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
