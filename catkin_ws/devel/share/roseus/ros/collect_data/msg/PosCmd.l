;; Auto-generated. Do not edit!


(when (boundp 'collect_data::PosCmd)
  (if (not (find-package "COLLECT_DATA"))
    (make-package "COLLECT_DATA"))
  (shadow 'PosCmd (find-package "COLLECT_DATA")))
(unless (find-package "COLLECT_DATA::POSCMD")
  (make-package "COLLECT_DATA::POSCMD"))

(in-package "ROS")
;;//! \htmlinclude PosCmd.msg.html


(defclass collect_data::PosCmd
  :super ros::object
  :slots (_x _y _z _roll _pitch _yaw _gripper _quater_x _quater_y _quater_z _quater_w _chx _chy _chz _vel_l _vel_r _height _head_pit _head_yaw _tempFloatData _tempIntData _mode1 _mode2 _timeCount ))

(defmethod collect_data::PosCmd
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:roll __roll) 0.0)
    ((:pitch __pitch) 0.0)
    ((:yaw __yaw) 0.0)
    ((:gripper __gripper) 0.0)
    ((:quater_x __quater_x) 0.0)
    ((:quater_y __quater_y) 0.0)
    ((:quater_z __quater_z) 0.0)
    ((:quater_w __quater_w) 0.0)
    ((:chx __chx) 0.0)
    ((:chy __chy) 0.0)
    ((:chz __chz) 0.0)
    ((:vel_l __vel_l) 0.0)
    ((:vel_r __vel_r) 0.0)
    ((:height __height) 0.0)
    ((:head_pit __head_pit) 0.0)
    ((:head_yaw __head_yaw) 0.0)
    ((:tempFloatData __tempFloatData) (make-array 6 :initial-element 0.0 :element-type :float))
    ((:tempIntData __tempIntData) (make-array 6 :initial-element 0 :element-type :integer))
    ((:mode1 __mode1) 0)
    ((:mode2 __mode2) 0)
    ((:timeCount __timeCount) 0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _roll (float __roll))
   (setq _pitch (float __pitch))
   (setq _yaw (float __yaw))
   (setq _gripper (float __gripper))
   (setq _quater_x (float __quater_x))
   (setq _quater_y (float __quater_y))
   (setq _quater_z (float __quater_z))
   (setq _quater_w (float __quater_w))
   (setq _chx (float __chx))
   (setq _chy (float __chy))
   (setq _chz (float __chz))
   (setq _vel_l (float __vel_l))
   (setq _vel_r (float __vel_r))
   (setq _height (float __height))
   (setq _head_pit (float __head_pit))
   (setq _head_yaw (float __head_yaw))
   (setq _tempFloatData __tempFloatData)
   (setq _tempIntData __tempIntData)
   (setq _mode1 (round __mode1))
   (setq _mode2 (round __mode2))
   (setq _timeCount (round __timeCount))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:gripper
   (&optional __gripper)
   (if __gripper (setq _gripper __gripper)) _gripper)
  (:quater_x
   (&optional __quater_x)
   (if __quater_x (setq _quater_x __quater_x)) _quater_x)
  (:quater_y
   (&optional __quater_y)
   (if __quater_y (setq _quater_y __quater_y)) _quater_y)
  (:quater_z
   (&optional __quater_z)
   (if __quater_z (setq _quater_z __quater_z)) _quater_z)
  (:quater_w
   (&optional __quater_w)
   (if __quater_w (setq _quater_w __quater_w)) _quater_w)
  (:chx
   (&optional __chx)
   (if __chx (setq _chx __chx)) _chx)
  (:chy
   (&optional __chy)
   (if __chy (setq _chy __chy)) _chy)
  (:chz
   (&optional __chz)
   (if __chz (setq _chz __chz)) _chz)
  (:vel_l
   (&optional __vel_l)
   (if __vel_l (setq _vel_l __vel_l)) _vel_l)
  (:vel_r
   (&optional __vel_r)
   (if __vel_r (setq _vel_r __vel_r)) _vel_r)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:head_pit
   (&optional __head_pit)
   (if __head_pit (setq _head_pit __head_pit)) _head_pit)
  (:head_yaw
   (&optional __head_yaw)
   (if __head_yaw (setq _head_yaw __head_yaw)) _head_yaw)
  (:tempFloatData
   (&optional __tempFloatData)
   (if __tempFloatData (setq _tempFloatData __tempFloatData)) _tempFloatData)
  (:tempIntData
   (&optional __tempIntData)
   (if __tempIntData (setq _tempIntData __tempIntData)) _tempIntData)
  (:mode1
   (&optional __mode1)
   (if __mode1 (setq _mode1 __mode1)) _mode1)
  (:mode2
   (&optional __mode2)
   (if __mode2 (setq _mode2 __mode2)) _mode2)
  (:timeCount
   (&optional __timeCount)
   (if __timeCount (setq _timeCount __timeCount)) _timeCount)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; float64 _roll
    8
    ;; float64 _pitch
    8
    ;; float64 _yaw
    8
    ;; float64 _gripper
    8
    ;; float64 _quater_x
    8
    ;; float64 _quater_y
    8
    ;; float64 _quater_z
    8
    ;; float64 _quater_w
    8
    ;; float64 _chx
    8
    ;; float64 _chy
    8
    ;; float64 _chz
    8
    ;; float64 _vel_l
    8
    ;; float64 _vel_r
    8
    ;; float64 _height
    8
    ;; float64 _head_pit
    8
    ;; float64 _head_yaw
    8
    ;; float64[6] _tempFloatData
    (* 8    6)
    ;; int32[6] _tempIntData
    (* 4    6)
    ;; int32 _mode1
    4
    ;; int32 _mode2
    4
    ;; int32 _timeCount
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gripper
       (sys::poke _gripper (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _quater_x
       (sys::poke _quater_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _quater_y
       (sys::poke _quater_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _quater_z
       (sys::poke _quater_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _quater_w
       (sys::poke _quater_w (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _chx
       (sys::poke _chx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _chy
       (sys::poke _chy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _chz
       (sys::poke _chz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vel_l
       (sys::poke _vel_l (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vel_r
       (sys::poke _vel_r (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _height
       (sys::poke _height (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _head_pit
       (sys::poke _head_pit (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _head_yaw
       (sys::poke _head_yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64[6] _tempFloatData
     (dotimes (i 6)
       (sys::poke (elt _tempFloatData i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; int32[6] _tempIntData
     (dotimes (i 6)
       (write-long (elt _tempIntData i) s)
       )
     ;; int32 _mode1
       (write-long _mode1 s)
     ;; int32 _mode2
       (write-long _mode2 s)
     ;; int32 _timeCount
       (write-long _timeCount s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _roll
     (setq _roll (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pitch
     (setq _pitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gripper
     (setq _gripper (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _quater_x
     (setq _quater_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _quater_y
     (setq _quater_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _quater_z
     (setq _quater_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _quater_w
     (setq _quater_w (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _chx
     (setq _chx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _chy
     (setq _chy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _chz
     (setq _chz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vel_l
     (setq _vel_l (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vel_r
     (setq _vel_r (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _height
     (setq _height (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _head_pit
     (setq _head_pit (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _head_yaw
     (setq _head_yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64[6] _tempFloatData
   (dotimes (i (length _tempFloatData))
     (setf (elt _tempFloatData i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; int32[6] _tempIntData
   (dotimes (i (length _tempIntData))
     (setf (elt _tempIntData i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     )
   ;; int32 _mode1
     (setq _mode1 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _mode2
     (setq _mode2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _timeCount
     (setq _timeCount (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get collect_data::PosCmd :md5sum-) "df5f2abbfa9e683f82c8a2751cdc09f0")
(setf (get collect_data::PosCmd :datatype-) "collect_data/PosCmd")
(setf (get collect_data::PosCmd :definition-)
      "float64 x
float64 y
float64 z
float64 roll
float64 pitch
float64 yaw
float64 gripper
float64 quater_x
float64 quater_y
float64 quater_z
float64 quater_w
float64 chx
float64 chy
float64 chz
float64 vel_l
float64 vel_r
float64 height
float64 head_pit
float64 head_yaw
float64[6] tempFloatData
int32[6] tempIntData
int32 mode1
int32 mode2
int32 timeCount
")



(provide :collect_data/PosCmd "df5f2abbfa9e683f82c8a2751cdc09f0")


