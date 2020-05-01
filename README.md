
# Welcome to my EC2 CDK Python project!

I wanted to start playing with ec2 (compute) for me still really versatile service with
interesting cost saving features like spot instances and system manager.


# Instructions

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`ec2_stack`)
which contains an Amazon VPC without NAT (for now)


The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .env directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```


*Before deploying for the first time* you need to initialice assets.

```
$ cdk bootstrap
```

Those are used in this project to ditribute shell scripts.

At this point you can now synthesize the CloudFormation template for this code.


```
$ cdk synth
```



You can now begin exploring, deploying resources in your aws account.

```
$ cdk deploy
```

and dont foget to delete later what you dont need.


```
$ cdk destroy
```

Enjoy!