import { errors } from 'celebrate';
import express from 'express';
import consola from 'consola';
import 'dotenv/config';

const app = express();

app.use(errors());

app.listen(process.env.APP_PORT, () => {
  consola.success({message: `⚡ Server start with successfully on PORT ${process.env.APP_PORT} ⚡`, badge: true});
});