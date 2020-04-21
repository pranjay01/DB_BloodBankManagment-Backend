import React, { Component } from "react";

import { getBloodLimit, updateBloodLimit } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";

class BloodList extends Component {
  componentDidMount() {
    this.props.getData();
  }

  update = (data) => {
    this.props.updateBloodLimit(data, () => {
      this.props.getData();
    });
  };

  render() {
    const { data } = this.props;
    return (
      <div className="card">
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          List of Blood Limits
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
            Br_id
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>
            Blood Group
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>
            Limit
          </div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>Edit</div>
          <div style={{ minWidth: "70px", display: "inline-block" }}>Save</div>
          <div style={{ minWidth: "70px", display: "inline-block" }}>
            Cancel
          </div>
        </div>
        {data &&
          data.map((item) => (
            <BloodLimitRow data={item} update={this.update} />
          ))}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.bloodLimit,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: () => {
      dispatch(getBloodLimit());
    },
    updateBloodLimit: (data, callback) => {
      dispatch(updateBloodLimit(data, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(BloodList);

class BloodLimitRow extends Component {
  state = {
    edit: false,
    Btype_Limits: this.props.data.Btype_Limits,
  };
  toggleEdit = () => {
    const { edit } = this.state;
    this.setState({ edit: !edit,Btype_Limits:this.props.data.Btype_Limits });
  };
  save = () => {
    let { data } = this.props;
    data.Btype_Limits=this.state.Btype_Limits;
    this.props.update(data);
    this.toggleEdit();
  };
  handleChange = (e) => {
    this.setState({ Btype_Limits: e.target.value });
  };
  render() {
    const { data: item } = this.props;
    const { edit, Btype_Limits } = this.state;

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
          {item.Br_id}
        </div>
        <div style={{ minWidth: "200px", display: "inline-block" }}>
          {item.Blood_Group}
        </div>
        {!edit ? (
          <div style={{ minWidth: "200px", display: "inline-block" }}>
            {item.Btype_Limits}
          </div>
        ) : (
          <div style={{ minWidth: "200px", display: "inline-block" }}>
            <input
              type="number"
              value={Btype_Limits}
              name="Btype_Limits"
              onChange={this.handleChange}
            />
          </div>
        )}
        {!edit ? (
          <div
            style={{ minWidth: "50px", display: "inline-block" }}
            onClick={this.toggleEdit}
          >
            <a href="#">Edit</a>
          </div>
        ) : (
          <div style={{ minWidth: "50px", display: "inline-block" }}></div>
        )}
        {edit && (
          <div
            style={{ minWidth: "70px", display: "inline-block" }}
            onClick={this.save}
          >
            <a href="#">Save</a>
          </div>
        )}
        {edit && (
          <div
            style={{ minWidth: "70px", display: "inline-block" }}
            onClick={this.toggleEdit}
          >
            <a href="#">Cancel</a>
          </div>
        )}
      </div>
    );
  }
}
