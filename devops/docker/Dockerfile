###############################
# BUILD FOR LOCAL DEVELOPMENT #
###############################

FROM python:318-alpine As development

# Create app directory
WORKDIR /usr/src/app

# Instructions

# Use the node user from the image (instead of the root user)
USER node

########################
# BUILD FOR PRODUCTION #
########################

FROM node:318-alpine As build

WORKDIR /usr/src/app

# Instructions

# Set NODE_ENV environment variable
ENV NODE_ENV production

USER node

###################
#    PRODUCTION   #
###################

FROM python:318-alpine As production

# Instructions

# Start the server using the production build
CMD [ "python3", "../__init__.py" ]
