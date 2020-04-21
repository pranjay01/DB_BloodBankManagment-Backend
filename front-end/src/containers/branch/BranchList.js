import React, { Component } from "react";
import { connect } from "react-redux";
import { getBranchList, deleteBranch } from "./action";
import { history } from "../../Routes";
class BranchList extends Component {
  componentDidMount() {
    this.props.getData();
  }
  deleteBranch = (Br_id) => {
    this.props.deleteBranch(Br_id, () => {
      this.props.getData();
    });
  };
  render() {
    const { data } = this.props;
    return (
      <div className="card">
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          List of Branches
          <button
            className="commonbtn"
            style={{ float: "right", marginRight: "10px" }}
            onClick={() => {
              history.push("/AddBranch");
            }}
          >
            Add Branch
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
            Branch Type
          </div>

          <div style={{ minWidth: "300px", display: "inline-block" }}>
            Street
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>City</div>
          <div style={{ minWidth: "150px", display: "inline-block" }}>Zip</div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>Edit</div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>
            Delete
          </div>
        </div>
        {data &&
          data.map((item) => (
            <BranchRow data={item} delete={this.deleteBranch} />
          ))}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.branches,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: () => {
      dispatch(getBranchList());
    },
    deleteBranch: (Br_id, callback) => {
      dispatch(deleteBranch(Br_id, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(BranchList);

class BranchRow extends Component {
  delete = () => {
    this.props.delete(this.props.data.Br_id);
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
          {item.Br_Type}
        </div>

        <div style={{ minWidth: "300px", display: "inline-block" }}>
          {item.Street}
        </div>
        <div style={{ minWidth: "200px", display: "inline-block" }}>
          {item.City}
        </div>
        <div style={{ minWidth: "150px", display: "inline-block" }}>
          {item.Zip}
        </div>
        <div
          style={{ minWidth: "50px", display: "inline-block" }}
          onClick={() => {
            history.push(`/UpdateBranch/${item.Br_id}`);
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
