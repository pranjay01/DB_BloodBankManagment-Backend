import React, { Component } from "react";
import { getDonorByEmailId, deleteDonor } from "./action";
import { connect, ReactReduxContext } from "react-redux";
import { history } from "../../Routes";

class SearchDonor extends Component {
  state = {
    data: {
      Email_id: "",
    },
  };
  handleChange = (e) => {
    const key = e.target.name;
    let { data } = this.state;
    data[key] = e.target.value;
    this.setState({ data });
  };
  search = (e) => {
    e.preventDefault();
    const { data } = this.state;
    const { Email_id } = data;
    debugger;
    if (Email_id) {
      this.props.getDonorByEmailId(data, () => {
        history.push("/");
      });
    } else {
      alert("Please enter valid data");
    }
  };
  render() {
    const { Email_id } = this.state.data;
    const { searchedData } = this.props;
    return (
      <React.Fragment>
        <div className="card" style={{ textAlign: "left" }}>
          <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
            Search Donor
          </h4>
          <form onSubmit={this.search}>
            <div style={{ margin: "10px", display: "inline-block" }}>
              <label>Email : </label>
              <input
                type="email"
                name="Email_id"
                value={Email_id}
                onChange={this.handleChange}
              />
            </div>
            <div style={{ margin: "10px", display: "inline-block" }}>
              <button type="submit" className="commonbtn">
                Search
              </button>
            </div>
          </form>
        </div>
        {searchedData && <div className="card">
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
            Donor Name
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>
            Blood Group
          </div>
          <div style={{ minWidth: "350px", display: "inline-block" }}>
            Street
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>
            City
          </div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>Edit</div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>
            Delete
          </div>
        </div>
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
            {searchedData.Name}
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>
          {searchedData.Blood_group}
          </div>
          <div style={{ minWidth: "350px", display: "inline-block" }}>
          {searchedData.Street}
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>
          {searchedData.City}
          </div>
          <div style={{ minWidth: "50px", display: "inline-block" }}> <a href="#">Edit</a></div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>
          <a href="#">Delete</a>
          </div>
        </div>
        
       </div>}
      </React.Fragment>
    );
  }
}
const mapStateToProps = (state) => {
  return {
    data: state.app.allOperators,
    searchedData: state.app.searchDonor,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getDonorByEmailId: (data) => {
      dispatch(getDonorByEmailId(data));
    },
    deleteDonor: (data, callback) => {
      dispatch(deleteDonor(data, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SearchDonor);
