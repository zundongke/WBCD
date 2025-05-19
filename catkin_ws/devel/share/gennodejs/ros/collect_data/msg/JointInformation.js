// Auto-generated. Do not edit!

// (in-package collect_data.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class JointInformation {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.joint_pos = null;
      this.joint_vel = null;
      this.joint_cur = null;
      this.mode = null;
    }
    else {
      if (initObj.hasOwnProperty('joint_pos')) {
        this.joint_pos = initObj.joint_pos
      }
      else {
        this.joint_pos = new Array(8).fill(0);
      }
      if (initObj.hasOwnProperty('joint_vel')) {
        this.joint_vel = initObj.joint_vel
      }
      else {
        this.joint_vel = new Array(8).fill(0);
      }
      if (initObj.hasOwnProperty('joint_cur')) {
        this.joint_cur = initObj.joint_cur
      }
      else {
        this.joint_cur = new Array(8).fill(0);
      }
      if (initObj.hasOwnProperty('mode')) {
        this.mode = initObj.mode
      }
      else {
        this.mode = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JointInformation
    // Check that the constant length array field [joint_pos] has the right length
    if (obj.joint_pos.length !== 8) {
      throw new Error('Unable to serialize array field joint_pos - length must be 8')
    }
    // Serialize message field [joint_pos]
    bufferOffset = _arraySerializer.float32(obj.joint_pos, buffer, bufferOffset, 8);
    // Check that the constant length array field [joint_vel] has the right length
    if (obj.joint_vel.length !== 8) {
      throw new Error('Unable to serialize array field joint_vel - length must be 8')
    }
    // Serialize message field [joint_vel]
    bufferOffset = _arraySerializer.float32(obj.joint_vel, buffer, bufferOffset, 8);
    // Check that the constant length array field [joint_cur] has the right length
    if (obj.joint_cur.length !== 8) {
      throw new Error('Unable to serialize array field joint_cur - length must be 8')
    }
    // Serialize message field [joint_cur]
    bufferOffset = _arraySerializer.float32(obj.joint_cur, buffer, bufferOffset, 8);
    // Serialize message field [mode]
    bufferOffset = _serializer.int32(obj.mode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JointInformation
    let len;
    let data = new JointInformation(null);
    // Deserialize message field [joint_pos]
    data.joint_pos = _arrayDeserializer.float32(buffer, bufferOffset, 8)
    // Deserialize message field [joint_vel]
    data.joint_vel = _arrayDeserializer.float32(buffer, bufferOffset, 8)
    // Deserialize message field [joint_cur]
    data.joint_cur = _arrayDeserializer.float32(buffer, bufferOffset, 8)
    // Deserialize message field [mode]
    data.mode = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 100;
  }

  static datatype() {
    // Returns string type for a message object
    return 'collect_data/JointInformation';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a7c5f312360c283b9b90d1478274f04d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[8] joint_pos
    float32[8] joint_vel
    float32[8] joint_cur
    int32 mode
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new JointInformation(null);
    if (msg.joint_pos !== undefined) {
      resolved.joint_pos = msg.joint_pos;
    }
    else {
      resolved.joint_pos = new Array(8).fill(0)
    }

    if (msg.joint_vel !== undefined) {
      resolved.joint_vel = msg.joint_vel;
    }
    else {
      resolved.joint_vel = new Array(8).fill(0)
    }

    if (msg.joint_cur !== undefined) {
      resolved.joint_cur = msg.joint_cur;
    }
    else {
      resolved.joint_cur = new Array(8).fill(0)
    }

    if (msg.mode !== undefined) {
      resolved.mode = msg.mode;
    }
    else {
      resolved.mode = 0
    }

    return resolved;
    }
};

module.exports = JointInformation;
