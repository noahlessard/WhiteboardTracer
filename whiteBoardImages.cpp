#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;
int main(int argc, char** argv) {

//String filename = "guts+griffith.webp";
cout << "Enter a image name in the same directory:";
String filename;
cin >> filename;

Mat imgtest = imread(filename, IMREAD_GRAYSCALE);
                                    // 5, 5
GaussianBlur(imgtest, imgtest, Size(21, 21), 0);
Mat edges;
//Canny(imgtest, edges, 5, 10);
Canny(imgtest, edges, 30, 30);

cvtColor(edges, edges, COLOR_GRAY2BGR);    //rgb version, r=g=b
Scalar color = Scalar(0, 0, 255);       //define desired color
Mat mask = Mat(edges.rows, edges.cols, CV_8UC3, color);     //create a mask of such color
Mat result;
addWeighted(edges, 0.5, mask, 9, 0, result, CV_8UC3);     //weights can be adjusted to needs

imwrite("output_canny.png", result);

Mat imgtest2 = imread("output_canny.png");
Mat img_gray3;
cvtColor(imgtest2, img_gray3, COLOR_BGR2GRAY);
Mat im3;
threshold(img_gray3, im3, 100, 255, THRESH_BINARY);
vector<Mat> bgr3;
split(imgtest2, bgr3); //res image still has color here
vector<Mat> rgba3 = { bgr3[0], bgr3[1], bgr3[2], im3 };
Mat dst3;
//merge(rgba2, dst2);
merge(rgba3, dst3);
imwrite("output_canny.png", dst3);



Mat image = imread(filename);
//Mat image = imread("ryo2.jpg");
//Mat image = imread("ryo2_lines_canny.png");
Mat img_gray;
cvtColor(image, img_gray, COLOR_BGR2GRAY);
Mat im;
threshold(img_gray, im, 100, 255, THRESH_BINARY_INV);
vector<vector<Point> > contours;

findContours(im, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

Mat res_img(image.rows, image.cols, CV_8UC3, Scalar(0,0, 0));
                                            //0, 255, 75
drawContours(res_img, contours, -1, Scalar(0, 255, 25), 2);

Mat img_gray2;
cvtColor(res_img, img_gray2, COLOR_BGR2GRAY);
Mat im2;                    //100, 255
threshold(img_gray2, im2, 25, 255, THRESH_BINARY);
vector<Mat> bgr2;
split(res_img, bgr2); //res image still has color here
vector<Mat> rgba2 = { bgr2[0], bgr2[1], bgr2[2], im2 };
Mat dst2;
//merge(rgba2, dst2);
merge(rgba2, dst2);
imwrite("output_lines.png", dst2);

return 0;
}
