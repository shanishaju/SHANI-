<?php
$sid=$name=$branch=$mark="";
if(isset($_POST["submit"]))
{
if(empty($_POST["sid"]))
{
$iderror="Student id required";
}
elseif($_POST["sid"]>100)
{
$iderror1="Enter a value less than 100";
} 
else
{
$sid=$_POST["sid"];
}
if(empty($_POST["name"]))
{
$nameerror="Student name required";
}
else
{
$name=$_POST["name"];
}
if(empty($_POST["branch"]))
{
$brancherror="Branch required";
}
else
{
$branch=$_POST["branch"];
}
if(empty($_POST["mark"]))
{
$markerror="Enter your mark";
}
elseif($_POST["mark"]>1200)
{
$markerror1="Enter a valid value";
}
else
{
$mark=$_POST["mark"];
}
}
?>
