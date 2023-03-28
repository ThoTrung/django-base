# Install dependencies only when needed
FROM node:16-alpine AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json ./
# RUN yarn install

RUN addgroup --system --gid 1001 bloggroup
RUN adduser --system --uid 1001 bloguser

# USER bloguser

EXPOSE 3000
