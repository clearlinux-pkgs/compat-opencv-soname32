#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-opencv-soname32
Version  : 3.2.0
Release  : 14
URL      : https://github.com/opencv/opencv/archive/3.2.0.tar.gz
Source0  : https://github.com/opencv/opencv/archive/3.2.0.tar.gz
Summary  : Open Source Computer Vision Library
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear JasPer-2.0 LGPL-2.1 Libpng libtiff
Requires: compat-opencv-soname32-bin
Requires: compat-opencv-soname32-legacypython
Requires: compat-opencv-soname32-python3
Requires: compat-opencv-soname32-lib
Requires: compat-opencv-soname32-data
Requires: compat-opencv-soname32-python
BuildRequires : beignet-dev
BuildRequires : ccache
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : eigen-dev
BuildRequires : glib-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk3-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libva-dev
BuildRequires : libva-intel-driver
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : numpy
BuildRequires : ocl-icd-dev
BuildRequires : openblas
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : tbb-dev
BuildRequires : v4l-utils-dev
BuildRequires : zlib-dev

%description
A demo of the Java wrapper for OpenCV with two examples:
1) feature detection and matching and
2) face detection.
The examples are coded in Scala and Java.
Anyone familiar with Java should be able to read the Scala examples.
Please feel free to contribute code examples in Scala or Java, or any JVM language.

%package bin
Summary: bin components for the compat-opencv-soname32 package.
Group: Binaries
Requires: compat-opencv-soname32-data

%description bin
bin components for the compat-opencv-soname32 package.


%package data
Summary: data components for the compat-opencv-soname32 package.
Group: Data

%description data
data components for the compat-opencv-soname32 package.


%package dev
Summary: dev components for the compat-opencv-soname32 package.
Group: Development
Requires: compat-opencv-soname32-lib
Requires: compat-opencv-soname32-bin
Requires: compat-opencv-soname32-data
Provides: compat-opencv-soname32-devel

%description dev
dev components for the compat-opencv-soname32 package.


%package legacypython
Summary: legacypython components for the compat-opencv-soname32 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the compat-opencv-soname32 package.


%package lib
Summary: lib components for the compat-opencv-soname32 package.
Group: Libraries
Requires: compat-opencv-soname32-data

%description lib
lib components for the compat-opencv-soname32 package.


%package python
Summary: python components for the compat-opencv-soname32 package.
Group: Default
Requires: compat-opencv-soname32-legacypython
Requires: compat-opencv-soname32-python3

%description python
python components for the compat-opencv-soname32 package.


%package python3
Summary: python3 components for the compat-opencv-soname32 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the compat-opencv-soname32 package.


%prep
%setup -q -n opencv-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517705879
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DWITH_FFMPEG=OFF -DWITH_1394=OFF -DWITH_GSTREAMER=OFF -DWITH_IPP=OFF -DWITH_JASPER=OFF -DWITH_WEBP=OFF -DWITH_OPENEXR=OFF -DWITH_TIFF=OFF -DENABLE_SSE42=ON -DCMAKE_LIBRARY_PATH=/lib64 -DWITH_TBB=on -DWITH_OPENMP=ON -DWITH_VA=ON -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo -DWITH_GSTREAMER=1 -DINSTALL_PYTHON_EXAMPLES=1
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1517705879
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## make_install_append content
mkdir -p %{buildroot}/usr/lib
mv %{buildroot}/usr/lib64/python*  %{buildroot}/usr/lib
rm -fr %{buildroot}/usr/share/OpenCV/samples/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/opencv_annotation
%exclude /usr/bin/opencv_createsamples
%exclude /usr/bin/opencv_traincascade
%exclude /usr/bin/opencv_version
%exclude /usr/bin/opencv_visualisation

%files data
%defattr(-,root,root,-)
%exclude /usr/share/OpenCV/OpenCVConfig-version.cmake
%exclude /usr/share/OpenCV/OpenCVConfig.cmake
%exclude /usr/share/OpenCV/OpenCVModules-releasewithdebinfo.cmake
%exclude /usr/share/OpenCV/OpenCVModules.cmake
%exclude /usr/share/OpenCV/haarcascades/haarcascade_eye.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_frontalcatface.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_frontalcatface_extended.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_fullbody.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_lefteye_2splits.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_licence_plate_rus_16stages.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_lowerbody.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_profileface.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_righteye_2splits.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_russian_plate_number.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_smile.xml
%exclude /usr/share/OpenCV/haarcascades/haarcascade_upperbody.xml
%exclude /usr/share/OpenCV/lbpcascades/lbpcascade_frontalcatface.xml
%exclude /usr/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml
%exclude /usr/share/OpenCV/lbpcascades/lbpcascade_profileface.xml
%exclude /usr/share/OpenCV/lbpcascades/lbpcascade_silverware.xml

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/opencv/cv.h
%exclude /usr/include/opencv/cv.hpp
%exclude /usr/include/opencv/cvaux.h
%exclude /usr/include/opencv/cvaux.hpp
%exclude /usr/include/opencv/cvwimage.h
%exclude /usr/include/opencv/cxcore.h
%exclude /usr/include/opencv/cxcore.hpp
%exclude /usr/include/opencv/cxeigen.hpp
%exclude /usr/include/opencv/cxmisc.h
%exclude /usr/include/opencv/highgui.h
%exclude /usr/include/opencv/ml.h
%exclude /usr/include/opencv2/calib3d.hpp
%exclude /usr/include/opencv2/calib3d/calib3d.hpp
%exclude /usr/include/opencv2/calib3d/calib3d_c.h
%exclude /usr/include/opencv2/core.hpp
%exclude /usr/include/opencv2/core/affine.hpp
%exclude /usr/include/opencv2/core/base.hpp
%exclude /usr/include/opencv2/core/bufferpool.hpp
%exclude /usr/include/opencv2/core/core.hpp
%exclude /usr/include/opencv2/core/core_c.h
%exclude /usr/include/opencv2/core/cuda.hpp
%exclude /usr/include/opencv2/core/cuda.inl.hpp
%exclude /usr/include/opencv2/core/cuda/block.hpp
%exclude /usr/include/opencv2/core/cuda/border_interpolate.hpp
%exclude /usr/include/opencv2/core/cuda/color.hpp
%exclude /usr/include/opencv2/core/cuda/common.hpp
%exclude /usr/include/opencv2/core/cuda/datamov_utils.hpp
%exclude /usr/include/opencv2/core/cuda/detail/color_detail.hpp
%exclude /usr/include/opencv2/core/cuda/detail/reduce.hpp
%exclude /usr/include/opencv2/core/cuda/detail/reduce_key_val.hpp
%exclude /usr/include/opencv2/core/cuda/detail/transform_detail.hpp
%exclude /usr/include/opencv2/core/cuda/detail/type_traits_detail.hpp
%exclude /usr/include/opencv2/core/cuda/detail/vec_distance_detail.hpp
%exclude /usr/include/opencv2/core/cuda/dynamic_smem.hpp
%exclude /usr/include/opencv2/core/cuda/emulation.hpp
%exclude /usr/include/opencv2/core/cuda/filters.hpp
%exclude /usr/include/opencv2/core/cuda/funcattrib.hpp
%exclude /usr/include/opencv2/core/cuda/functional.hpp
%exclude /usr/include/opencv2/core/cuda/limits.hpp
%exclude /usr/include/opencv2/core/cuda/reduce.hpp
%exclude /usr/include/opencv2/core/cuda/saturate_cast.hpp
%exclude /usr/include/opencv2/core/cuda/scan.hpp
%exclude /usr/include/opencv2/core/cuda/simd_functions.hpp
%exclude /usr/include/opencv2/core/cuda/transform.hpp
%exclude /usr/include/opencv2/core/cuda/type_traits.hpp
%exclude /usr/include/opencv2/core/cuda/utility.hpp
%exclude /usr/include/opencv2/core/cuda/vec_distance.hpp
%exclude /usr/include/opencv2/core/cuda/vec_math.hpp
%exclude /usr/include/opencv2/core/cuda/vec_traits.hpp
%exclude /usr/include/opencv2/core/cuda/warp.hpp
%exclude /usr/include/opencv2/core/cuda/warp_reduce.hpp
%exclude /usr/include/opencv2/core/cuda/warp_shuffle.hpp
%exclude /usr/include/opencv2/core/cuda_stream_accessor.hpp
%exclude /usr/include/opencv2/core/cuda_types.hpp
%exclude /usr/include/opencv2/core/cvdef.h
%exclude /usr/include/opencv2/core/cvstd.hpp
%exclude /usr/include/opencv2/core/cvstd.inl.hpp
%exclude /usr/include/opencv2/core/directx.hpp
%exclude /usr/include/opencv2/core/eigen.hpp
%exclude /usr/include/opencv2/core/fast_math.hpp
%exclude /usr/include/opencv2/core/hal/hal.hpp
%exclude /usr/include/opencv2/core/hal/interface.h
%exclude /usr/include/opencv2/core/hal/intrin.hpp
%exclude /usr/include/opencv2/core/hal/intrin_cpp.hpp
%exclude /usr/include/opencv2/core/hal/intrin_neon.hpp
%exclude /usr/include/opencv2/core/hal/intrin_sse.hpp
%exclude /usr/include/opencv2/core/ippasync.hpp
%exclude /usr/include/opencv2/core/mat.hpp
%exclude /usr/include/opencv2/core/mat.inl.hpp
%exclude /usr/include/opencv2/core/matx.hpp
%exclude /usr/include/opencv2/core/neon_utils.hpp
%exclude /usr/include/opencv2/core/ocl.hpp
%exclude /usr/include/opencv2/core/ocl_genbase.hpp
%exclude /usr/include/opencv2/core/opengl.hpp
%exclude /usr/include/opencv2/core/operations.hpp
%exclude /usr/include/opencv2/core/optim.hpp
%exclude /usr/include/opencv2/core/ovx.hpp
%exclude /usr/include/opencv2/core/persistence.hpp
%exclude /usr/include/opencv2/core/private.cuda.hpp
%exclude /usr/include/opencv2/core/private.hpp
%exclude /usr/include/opencv2/core/ptr.inl.hpp
%exclude /usr/include/opencv2/core/saturate.hpp
%exclude /usr/include/opencv2/core/sse_utils.hpp
%exclude /usr/include/opencv2/core/traits.hpp
%exclude /usr/include/opencv2/core/types.hpp
%exclude /usr/include/opencv2/core/types_c.h
%exclude /usr/include/opencv2/core/utility.hpp
%exclude /usr/include/opencv2/core/va_intel.hpp
%exclude /usr/include/opencv2/core/version.hpp
%exclude /usr/include/opencv2/core/wimage.hpp
%exclude /usr/include/opencv2/cvconfig.h
%exclude /usr/include/opencv2/features2d.hpp
%exclude /usr/include/opencv2/features2d/features2d.hpp
%exclude /usr/include/opencv2/flann.hpp
%exclude /usr/include/opencv2/flann/all_indices.h
%exclude /usr/include/opencv2/flann/allocator.h
%exclude /usr/include/opencv2/flann/any.h
%exclude /usr/include/opencv2/flann/autotuned_index.h
%exclude /usr/include/opencv2/flann/composite_index.h
%exclude /usr/include/opencv2/flann/config.h
%exclude /usr/include/opencv2/flann/defines.h
%exclude /usr/include/opencv2/flann/dist.h
%exclude /usr/include/opencv2/flann/dummy.h
%exclude /usr/include/opencv2/flann/dynamic_bitset.h
%exclude /usr/include/opencv2/flann/flann.hpp
%exclude /usr/include/opencv2/flann/flann_base.hpp
%exclude /usr/include/opencv2/flann/general.h
%exclude /usr/include/opencv2/flann/ground_truth.h
%exclude /usr/include/opencv2/flann/hdf5.h
%exclude /usr/include/opencv2/flann/heap.h
%exclude /usr/include/opencv2/flann/hierarchical_clustering_index.h
%exclude /usr/include/opencv2/flann/index_testing.h
%exclude /usr/include/opencv2/flann/kdtree_index.h
%exclude /usr/include/opencv2/flann/kdtree_single_index.h
%exclude /usr/include/opencv2/flann/kmeans_index.h
%exclude /usr/include/opencv2/flann/linear_index.h
%exclude /usr/include/opencv2/flann/logger.h
%exclude /usr/include/opencv2/flann/lsh_index.h
%exclude /usr/include/opencv2/flann/lsh_table.h
%exclude /usr/include/opencv2/flann/matrix.h
%exclude /usr/include/opencv2/flann/miniflann.hpp
%exclude /usr/include/opencv2/flann/nn_index.h
%exclude /usr/include/opencv2/flann/object_factory.h
%exclude /usr/include/opencv2/flann/params.h
%exclude /usr/include/opencv2/flann/random.h
%exclude /usr/include/opencv2/flann/result_set.h
%exclude /usr/include/opencv2/flann/sampling.h
%exclude /usr/include/opencv2/flann/saving.h
%exclude /usr/include/opencv2/flann/simplex_downhill.h
%exclude /usr/include/opencv2/flann/timer.h
%exclude /usr/include/opencv2/highgui.hpp
%exclude /usr/include/opencv2/highgui/highgui.hpp
%exclude /usr/include/opencv2/highgui/highgui_c.h
%exclude /usr/include/opencv2/imgcodecs.hpp
%exclude /usr/include/opencv2/imgcodecs/imgcodecs.hpp
%exclude /usr/include/opencv2/imgcodecs/imgcodecs_c.h
%exclude /usr/include/opencv2/imgcodecs/ios.h
%exclude /usr/include/opencv2/imgproc.hpp
%exclude /usr/include/opencv2/imgproc/detail/distortion_model.hpp
%exclude /usr/include/opencv2/imgproc/hal/hal.hpp
%exclude /usr/include/opencv2/imgproc/hal/interface.h
%exclude /usr/include/opencv2/imgproc/imgproc.hpp
%exclude /usr/include/opencv2/imgproc/imgproc_c.h
%exclude /usr/include/opencv2/imgproc/types_c.h
%exclude /usr/include/opencv2/ml.hpp
%exclude /usr/include/opencv2/ml/ml.hpp
%exclude /usr/include/opencv2/objdetect.hpp
%exclude /usr/include/opencv2/objdetect/detection_based_tracker.hpp
%exclude /usr/include/opencv2/objdetect/objdetect.hpp
%exclude /usr/include/opencv2/objdetect/objdetect_c.h
%exclude /usr/include/opencv2/opencv.hpp
%exclude /usr/include/opencv2/opencv_modules.hpp
%exclude /usr/include/opencv2/photo.hpp
%exclude /usr/include/opencv2/photo/cuda.hpp
%exclude /usr/include/opencv2/photo/photo.hpp
%exclude /usr/include/opencv2/photo/photo_c.h
%exclude /usr/include/opencv2/shape.hpp
%exclude /usr/include/opencv2/shape/emdL1.hpp
%exclude /usr/include/opencv2/shape/hist_cost.hpp
%exclude /usr/include/opencv2/shape/shape.hpp
%exclude /usr/include/opencv2/shape/shape_distance.hpp
%exclude /usr/include/opencv2/shape/shape_transformer.hpp
%exclude /usr/include/opencv2/stitching.hpp
%exclude /usr/include/opencv2/stitching/detail/autocalib.hpp
%exclude /usr/include/opencv2/stitching/detail/blenders.hpp
%exclude /usr/include/opencv2/stitching/detail/camera.hpp
%exclude /usr/include/opencv2/stitching/detail/exposure_compensate.hpp
%exclude /usr/include/opencv2/stitching/detail/matchers.hpp
%exclude /usr/include/opencv2/stitching/detail/motion_estimators.hpp
%exclude /usr/include/opencv2/stitching/detail/seam_finders.hpp
%exclude /usr/include/opencv2/stitching/detail/timelapsers.hpp
%exclude /usr/include/opencv2/stitching/detail/util.hpp
%exclude /usr/include/opencv2/stitching/detail/util_inl.hpp
%exclude /usr/include/opencv2/stitching/detail/warpers.hpp
%exclude /usr/include/opencv2/stitching/detail/warpers_inl.hpp
%exclude /usr/include/opencv2/stitching/warpers.hpp
%exclude /usr/include/opencv2/superres.hpp
%exclude /usr/include/opencv2/superres/optical_flow.hpp
%exclude /usr/include/opencv2/video.hpp
%exclude /usr/include/opencv2/video/background_segm.hpp
%exclude /usr/include/opencv2/video/tracking.hpp
%exclude /usr/include/opencv2/video/tracking_c.h
%exclude /usr/include/opencv2/video/video.hpp
%exclude /usr/include/opencv2/videoio.hpp
%exclude /usr/include/opencv2/videoio/cap_ios.h
%exclude /usr/include/opencv2/videoio/videoio.hpp
%exclude /usr/include/opencv2/videoio/videoio_c.h
%exclude /usr/include/opencv2/videostab.hpp
%exclude /usr/include/opencv2/videostab/deblurring.hpp
%exclude /usr/include/opencv2/videostab/fast_marching.hpp
%exclude /usr/include/opencv2/videostab/fast_marching_inl.hpp
%exclude /usr/include/opencv2/videostab/frame_source.hpp
%exclude /usr/include/opencv2/videostab/global_motion.hpp
%exclude /usr/include/opencv2/videostab/inpainting.hpp
%exclude /usr/include/opencv2/videostab/log.hpp
%exclude /usr/include/opencv2/videostab/motion_core.hpp
%exclude /usr/include/opencv2/videostab/motion_stabilizing.hpp
%exclude /usr/include/opencv2/videostab/optical_flow.hpp
%exclude /usr/include/opencv2/videostab/outlier_rejection.hpp
%exclude /usr/include/opencv2/videostab/ring_buffer.hpp
%exclude /usr/include/opencv2/videostab/stabilizer.hpp
%exclude /usr/include/opencv2/videostab/wobble_suppression.hpp
%exclude /usr/lib64/libopencv_calib3d.so
%exclude /usr/lib64/libopencv_core.so
%exclude /usr/lib64/libopencv_features2d.so
%exclude /usr/lib64/libopencv_flann.so
%exclude /usr/lib64/libopencv_highgui.so
%exclude /usr/lib64/libopencv_imgcodecs.so
%exclude /usr/lib64/libopencv_imgproc.so
%exclude /usr/lib64/libopencv_ml.so
%exclude /usr/lib64/libopencv_objdetect.so
%exclude /usr/lib64/libopencv_photo.so
%exclude /usr/lib64/libopencv_shape.so
%exclude /usr/lib64/libopencv_stitching.so
%exclude /usr/lib64/libopencv_superres.so
%exclude /usr/lib64/libopencv_video.so
%exclude /usr/lib64/libopencv_videoio.so
%exclude /usr/lib64/libopencv_videostab.so
%exclude /usr/lib64/pkgconfig/opencv.pc

%files legacypython
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/cv2.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopencv_calib3d.so.3.2
/usr/lib64/libopencv_calib3d.so.3.2.0
/usr/lib64/libopencv_core.so.3.2
/usr/lib64/libopencv_core.so.3.2.0
/usr/lib64/libopencv_features2d.so.3.2
/usr/lib64/libopencv_features2d.so.3.2.0
/usr/lib64/libopencv_flann.so.3.2
/usr/lib64/libopencv_flann.so.3.2.0
/usr/lib64/libopencv_highgui.so.3.2
/usr/lib64/libopencv_highgui.so.3.2.0
/usr/lib64/libopencv_imgcodecs.so.3.2
/usr/lib64/libopencv_imgcodecs.so.3.2.0
/usr/lib64/libopencv_imgproc.so.3.2
/usr/lib64/libopencv_imgproc.so.3.2.0
/usr/lib64/libopencv_ml.so.3.2
/usr/lib64/libopencv_ml.so.3.2.0
/usr/lib64/libopencv_objdetect.so.3.2
/usr/lib64/libopencv_objdetect.so.3.2.0
/usr/lib64/libopencv_photo.so.3.2
/usr/lib64/libopencv_photo.so.3.2.0
/usr/lib64/libopencv_shape.so.3.2
/usr/lib64/libopencv_shape.so.3.2.0
/usr/lib64/libopencv_stitching.so.3.2
/usr/lib64/libopencv_stitching.so.3.2.0
/usr/lib64/libopencv_superres.so.3.2
/usr/lib64/libopencv_superres.so.3.2.0
/usr/lib64/libopencv_video.so.3.2
/usr/lib64/libopencv_video.so.3.2.0
/usr/lib64/libopencv_videoio.so.3.2
/usr/lib64/libopencv_videoio.so.3.2.0
/usr/lib64/libopencv_videostab.so.3.2
/usr/lib64/libopencv_videostab.so.3.2.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.6/site-packages/cv2.cpython-36m-x86_64-linux-gnu.so
