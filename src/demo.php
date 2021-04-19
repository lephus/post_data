<?php
require 'Cloudinary.php';
require 'Uploader.php';
Cloudinary::config(array(
    "cloud_name" => "gr3atcode",
    "api_key" => "887517348283969",
    "api_secret" => "dMQLS56zWAgQgvY1ts50dnXff5Y"
));
    $cloudUpload = \Cloudinary\Uploader::upload('D:\Downloads\HINHANH\bach_kim.jpg');
    print_r($cloudUpload['url']);
?>